"use client";

import { useEffect, useState } from "react";
import axios from "axios";

export default function Home() {
  const [stats, setStats] = useState<any>(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/dashboard")
      .then((res) => setStats(res.data))
      .catch((err) => console.error(err));
  }, []);

  if (!stats) {
    return (
      <div className="p-10">
        <h1>Loading Dashboard...</h1>
      </div>
    );
  }

  return (
    <main className="min-h-screen p-10">
      <h1 className="text-4xl font-bold mb-8">
        AI Gmail Intelligence Dashboard
      </h1>

      <div className="grid grid-cols-2 gap-6">

        <div className="border rounded-xl p-6">
          <h2 className="text-xl font-semibold">Total Emails</h2>
          <p className="text-3xl">{stats.total_emails}</p>
        </div>

        <div className="border rounded-xl p-6">
          <h2 className="text-xl font-semibold">Job Emails</h2>
          <p className="text-3xl">{stats.job_emails}</p>
        </div>

        <div className="border rounded-xl p-6">
          <h2 className="text-xl font-semibold">Security Emails</h2>
          <p className="text-3xl">{stats.security_emails}</p>
        </div>

        <div className="border rounded-xl p-6">
          <h2 className="text-xl font-semibold">Education Emails</h2>
          <p className="text-3xl">{stats.education_emails}</p>
        </div>

      </div>
    </main>
  );
}