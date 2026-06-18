"use client";

import { useEffect, useState } from "react";
import axios from "axios";

export default function SecurityPage() {
  const [securityEmails, setSecurityEmails] = useState<any[]>([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/emails/security")
      .then((res) => setSecurityEmails(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-4xl font-bold mb-6">
        Security Emails
      </h1>

      {securityEmails.map((email) => (
        <div
          key={email.id}
          className="border p-4 rounded-lg mb-4"
        >
          <h2 className="font-bold">
            {email.subject}
          </h2>

          <p>{email.sender}</p>

          <p className="mt-2">
            {email.summary}
          </p>
        </div>
      ))}
    </main>
  );
}