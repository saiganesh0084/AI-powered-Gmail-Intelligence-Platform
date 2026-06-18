export default function Navbar() {
  return (
    <nav className="flex gap-6 p-4 border-b text-lg">
      <a href="/">Dashboard</a>
      <a href="/jobs">Jobs</a>
      <a href="/security">Security</a>
      <a href="/assistant">AI Assistant</a>
    </nav>
  );
}