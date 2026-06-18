# AI Gmail Intelligence Platform

## Overview

AI Gmail Intelligence Platform is a full-stack AI-powered email management system that integrates with Gmail using OAuth 2.0, synchronizes email data, stores it in Supabase, and provides AI-driven insights through email summarization, categorization, and conversational querying.

The platform enables users to:

* Connect their Gmail account securely
* Synchronize emails from Gmail API
* Automatically clean and process email content
* Categorize emails using AI
* Generate concise summaries for emails
* Query emails using a conversational AI assistant
* View categorized emails through an interactive dashboard

---

## Features

### Gmail Integration

* Gmail OAuth 2.0 Authentication
* Gmail API Inbox Synchronization
* Message Metadata Extraction
* Thread Tracking
* Secure Access Token Handling

### Email Processing

* HTML Email Cleaning
* Plain Text Extraction
* Email Metadata Parsing
* Sender Identification
* Subject Extraction

### AI Features

* Email Categorization
* Email Summarization
* AI Email Assistant
* Context-Aware Email Querying

### Dashboard

* Total Email Statistics
* Category-Based Insights
* Job Email Tracking
* Security Email Tracking
* Education Email Tracking

### Email Management

* Email Detail View
* Category Filtering
* Searchable Email Repository

---

## Tech Stack

### Frontend

* Next.js 15
* React
* TypeScript
* Tailwind CSS
* Axios

### Backend

* FastAPI
* Python

### Database

* Supabase
* PostgreSQL

### AI

* Google Gemini API

### Integrations

* Gmail API
* Google OAuth 2.0

---

## Project Structure

```text
gmail-intelligence/

├── backend/
│
├── main.py
├── gmail_auth.py
├── gemini_client.py
├── supabase_client.py
├── test_gemini.py
├── .env
├── requirements.txt
│
└── frontend/
│
├── app/
│   ├── page.tsx
│   ├── jobs/
│   │   └── page.tsx
│   ├── security/
│   │   └── page.tsx
│   ├── assistant/
│   │   └── page.tsx
│   ├── emails/
│   │   └── [id]/
│   │       └── page.tsx
│   ├── components/
│   │   └── Navbar.tsx
│   ├── layout.tsx
│   └── globals.css
│
├── README.md
├── Architecture.md
└── .env.example
```

---

## Environment Variables

Backend (.env)

```env
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=

GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

GEMINI_API_KEY=
```

---

## Installation

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

## API Endpoints

### Authentication

```http
GET /login
```

Authenticate Gmail Account

---

### Email Synchronization

```http
GET /auth/callback
```

Synchronize emails and store in Supabase

---

### Dashboard

```http
GET /dashboard
```

Returns dashboard statistics

---

### Email Categories

```http
GET /emails/jobs

GET /emails/security

GET /emails/education
```

---

### AI Assistant

```http
GET /ask?q=
```

Ask questions about stored emails

---

## Future Improvements

* Thread-Level Summaries
* Incremental Gmail Sync
* pgvector Semantic Search
* Email Compose & Reply
* Newsletter Deduplication
* Multi-User Support
* Deployment & CI/CD

---

## Author

Ganoju Sai Ganesh

saiganeshganoju@gmail.com

B.Tech CSE (AI & ML)

AI Automation Executive Technical Assessment Submission
