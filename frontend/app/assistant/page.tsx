"use client";

import { useState } from "react";
import axios from "axios";

export default function AssistantPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askAI = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/ask?q=${encodeURIComponent(question)}`
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <main className="p-10">
      <h1 className="text-4xl font-bold mb-6">
        AI Email Assistant
      </h1>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask about your emails..."
        className="border p-3 w-full rounded-lg text-black"
      />

      <button
        onClick={askAI}
        className="mt-4 border px-6 py-3 rounded-lg"
      >
        Ask
      </button>

      {answer && (
        <div className="mt-8 border p-4 rounded-lg">
          <h2 className="font-bold mb-2">Answer</h2>
          <p>{answer}</p>
        </div>
      )}
    </main>
  );
}