"use client";

import { useEffect, useState } from "react";
import axios from "axios";

export default function JobsPage() {
  const [jobs, setJobs] = useState<any[]>([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/emails/jobs")
      .then((res) => setJobs(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-4xl font-bold mb-6">
        Job Emails
      </h1>

      {jobs.map((job) => (
        <div
          key={job.id}
          className="border p-4 rounded-lg mb-4"
        >
          <a 
            href={`/emails/${job.gmail_message_id}`}
            className="font-bold text-blue-500"
          >
            {job.subject}
          </a>

          <p>{job.sender}</p>

          <p className="mt-2">
            {job.summary}
          </p>
        </div>
      ))}
    </main>
  );
}