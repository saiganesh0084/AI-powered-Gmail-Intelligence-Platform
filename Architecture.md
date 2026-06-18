# Architecture & Design Document

## System Architecture

```text
┌─────────────────┐
│ Gmail API       │
└────────┬────────┘
         │ OAuth 2.0
         ▼
┌─────────────────┐
│ FastAPI Backend │
└────────┬────────┘
         │
         ├────────► Gmail Synchronization
         │
         ├────────► Email Cleaning
         │
         ├────────► Gemini Analysis
         │
         ▼
┌─────────────────┐
│ Supabase        │
│ PostgreSQL      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Next.js Frontend│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ AI Assistant    │
└─────────────────┘
```

---

## Database Schema

### emails

| Column           | Type      |
| ---------------- | --------- |
| id               | UUID      |
| gmail_message_id | TEXT      |
| gmail_thread_id  | TEXT      |
| sender           | TEXT      |
| subject          | TEXT      |
| body             | TEXT      |
| category         | TEXT      |
| summary          | TEXT      |
| created_at       | TIMESTAMP |

### Purpose

Stores processed Gmail messages along with AI-generated metadata.

---

## AI Design

### Categorization

Gemini analyzes:

* Subject
* Sender
* Email Body

Outputs:

```json
{
  "category": "Job Opportunity",
  "summary": "..."
}
```

### Summarization

Each email is summarized individually to provide concise insights while reducing token usage.

### AI Assistant

The assistant retrieves stored emails from Supabase and provides answers based on email summaries and metadata.

---

## Gmail API Strategy

### Authentication

OAuth 2.0 Authorization Code Flow

### Synchronization

Current implementation:

* Fetch latest emails
* Extract metadata
* Store in Supabase

### Future Enhancements

* Incremental Sync
* Pagination
* Background Processing
* Rate Limit Handling

---

## Technology Decisions

### FastAPI

Chosen for:

* High performance
* Simple API creation
* Async support

### Next.js

Chosen for:

* Modern React framework
* Excellent developer experience
* Easy deployment

### Supabase

Chosen for:

* Managed PostgreSQL
* Authentication support
* Scalable architecture

### Gemini

Chosen for:

* Strong summarization
* Classification capabilities
* Easy API integration

---

## Trade-Offs & Limitations

### Current Limitations

* No thread-level reasoning
* No email compose/reply workflow
* No pgvector implementation
* No newsletter deduplication

### Future Improvements

* Vector embeddings
* Semantic retrieval
* Thread-aware conversations
* Advanced AI workflows
* Multi-user support
