import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_email(subject, body):

    prompt = f"""
Analyze this email.

Subject:
{subject}

Body:
{body[:3000]}

Return ONLY valid JSON.

{{
    "category": "",
    "summary": ""
}}

Categories:
- Job Opportunity
- Newsletter
- Security
- Finance
- Personal
- Education
- Other
"""

    response = model.generate_content(prompt)

    return response.text


def ask_email_assistant(context, question):

    prompt = f"""
You are an AI Email Assistant.

Use ONLY the emails below.

EMAILS:
{context}

USER QUESTION:
{question}

Give a direct answer.
Do not return JSON.
Do not categorize.
Answer in plain English.
"""

    response = model.generate_content(prompt)

    return response.text