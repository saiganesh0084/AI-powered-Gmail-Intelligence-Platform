from fastapi.middleware.cors import CORSMiddleware
from supabase_client import supabase
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from googleapiclient.discovery import build
from gmail_auth import create_flow
from gemini_client import analyze_email
from bs4 import BeautifulSoup
from fastapi import Query
from gemini_client import ask_email_assistant
import json
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth_flow = None


@app.get("/")
def home():
    return {"message": "AI Gmail Intelligence Platform"}


@app.get("/login")
def login():
    global oauth_flow

    oauth_flow = create_flow()

    auth_url, state = oauth_flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )

    return RedirectResponse(auth_url)


@app.get("/auth/callback")
def auth_callback(code: str):

    global oauth_flow

    oauth_flow.fetch_token(code=code)

    credentials = oauth_flow.credentials

    service = build(
        "gmail",
        "v1",
        credentials=credentials
    )

    results = service.users().messages().list(
        userId="me",
        maxResults=10
    ).execute()

    messages = results.get("messages", [])

    email_data = []

    for msg in messages:

        message = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = message["payload"].get("headers", [])

        subject = ""
        sender = ""
        body = ""

        # Extract subject and sender
        for header in headers:

            if header["name"] == "Subject":
                subject = header["value"]

            if header["name"] == "From":
                sender = header["value"]

        # Extract body
        if "parts" in message["payload"]:

            for part in message["payload"]["parts"]:

                if part["mimeType"] == "text/plain":

                    data = part["body"].get("data")

                    if data:
                        try:
                            body = base64.urlsafe_b64decode(
                                data
                            ).decode("utf-8", errors="ignore")
                        except Exception:
                            body = ""

        elif "body" in message["payload"]:

            data = message["payload"]["body"].get("data")

            if data:
                try:
                    body = base64.urlsafe_b64decode(
                        data
                    ).decode("utf-8", errors="ignore")
                except Exception:
                    body = ""

        # Clean HTML emails
        clean_body = body

        if "<html" in body.lower() or "<body" in body.lower():

            soup = BeautifulSoup(
                body,
                "html.parser"
            )

            clean_body = soup.get_text(
                separator=" ",
                strip=True
            )

        # Gemini Analysis
        try:

            analysis = analyze_email(
                subject,
                clean_body
            )

            analysis = analysis.replace(
                "```json",
                ""
            )

            analysis = analysis.replace(
                "```",
                ""
            )

            result = json.loads(
                analysis.strip()
            )

            category = result.get(
                "category",
                "Other"
            )

            summary = result.get(
                "summary",
                ""
            )

        except Exception as e:
		    
            print("GEMINI ERROR:", str(e))

            category = "Other"

            summary = (
                f"Error: {str(e)}"
            )

        # Save to Supabase
        supabase.table("emails").upsert(
            {
                "gmail_message_id": msg["id"],
                "gmail_thread_id": msg["threadId"],
                "sender": sender,
                "subject": subject,
                "body": clean_body,
                "category": category,
                "summary": summary
            },
            on_conflict="gmail_message_id"
        ).execute()

        # API Response
        email_data.append(
            {
                "id": msg["id"],
                "threadId": msg["threadId"],
                "subject": subject,
                "sender": sender,
                "category": category,
                "summary": summary
            }
        )

    return {
        "total_emails": len(email_data),
        "emails": email_data
    }
@app.get("/dashboard")
def dashboard():

    emails = supabase.table("emails").select("*").execute()

    data = emails.data

    return {
        "total_emails": len(data),
        "job_emails": len([e for e in data if e["category"] == "Job Opportunity"]),
        "security_emails": len([e for e in data if e["category"] == "Security"]),
        "education_emails": len([e for e in data if e["category"] == "Education"]),
        "finance_emails": len([e for e in data if e["category"] == "Finance"])
    }
@app.get("/emails/jobs")
def job_emails():

    result = supabase.table("emails") \
        .select("*") \
        .eq("category", "Job Opportunity") \
        .execute()

    return result.data
@app.get("/emails/security")
def security_emails():

    result = supabase.table("emails") \
        .select("*") \
        .eq("category", "Security") \
        .execute()

    return result.data
@app.get("/emails/education")
def education_emails():

    result = supabase.table("emails") \
        .select("*") \
        .eq("category", "Education") \
        .execute()

    return result.data
@app.get("/ask")
def ask_ai(q: str = Query(...)):

    emails = supabase.table("emails") \
        .select("subject, sender, category, summary") \
        .execute()

    email_context = ""

    for email in emails.data:

        email_context += f"""
Subject: {email['subject']}
Sender: {email['sender']}
Category: {email['category']}
Summary: {email['summary']}

"""

    answer = ask_email_assistant(
        email_context,
        q
    )

    return {
        "question": q,
        "answer": answer
    }
@app.get("/email/{email_id}")
def get_email(email_id: str):

    result = (
        supabase.table("emails")
        .select("*")
        .eq("gmail_message_id", email_id)
        .execute()
    )

    if not result.data:
        return {"error": "Email not found"}

    return result.data[0]