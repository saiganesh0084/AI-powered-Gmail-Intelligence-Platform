"use client";

import axios from "axios";
import { useEffect, useState } from "react";

export default function EmailPage({
  params,
}: {
  params: { id: string };
}) {
  const [email, setEmail] = useState<any>(null);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/email/${params.id}`)
      .then((res) => setEmail(res.data))
      .catch((err) => console.error(err));
  }, [params.id]);

  if (!email) {
    return <div className="p-10">Loading...</div>;
  }

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold mb-4">
        {email.subject}
      </h1>

      <p>
        <strong>Sender:</strong> {email.sender}
      </p>

      <p>
        <strong>Category:</strong> {email.category}
      </p>

      <div className="mt-6">
        <h2 className="text-xl font-bold">
          Summary
        </h2>

        <p>{email.summary}</p>
      </div>

      <div className="mt-6">
        <h2 className="text-xl font-bold">
          Body
        </h2>

        <p className="whitespace-pre-wrap">
          {email.body}
        </p>
      </div>
    </main>
  );
}