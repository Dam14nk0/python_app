import React from "react";
import DashboardPage from "./pages/DashboardPage";

const courseData = {
  category: "Programming",
  track: "Python",
  title: "Python for Pentesters",
  modules: [
    {
      id: "m1",
      title: "Basics",
      progress: "3/14",
      days: [
        { day: 1, title: "What is Python", status: "done" },
        { day: 2, title: "Variables & input", status: "done" },
        { day: 3, title: "Why loops matter", status: "active" },
        { day: 4, title: "Functions explained", status: "locked" },
      ],
    },
    {
      id: "m2",
      title: "Files & Automation",
      progress: "0/16",
      days: [
        { day: 15, title: "Reading files safely", status: "locked" },
        { day: 16, title: "Writing reports", status: "locked" },
      ],
    },
  ],
};

const lesson = {
  day: 3,
  title: "Why loops exist and how to use them safely",
  intro:
    "You have zero Python background. Today we explain what loops are, why they matter in pentesting, and how one mistake can break automation.",
  kpis: [
    { icon: "⚡", label: "XP", value: "1,240" },
    { icon: "🛡️", label: "Level", value: "Beginner" },
    { icon: "📈", label: "Completion", value: "3%" },
    { icon: "🔥", label: "Streak", value: "2 days" },
  ],
  callouts: [
    { type: "idea", title: "What it is", text: "A loop repeats a block so you do not copy-paste actions." },
    { type: "mistake", title: "Common mistake", text: "Infinite loops happen when stop condition is never updated." },
    { type: "pro", title: "Why it matters", text: "Pentest scripts scan many targets. Loops make that possible." },
  ],
  steps: [
    "Read one host from a list and print it.",
    "Repeat for all hosts using a for-loop.",
    "Skip empty host entries safely.",
    "Print processed host count.",
  ],
  tasks: [
    { text: "Explain loop in your own words", done: true },
    { text: "Run the provided for-loop example", done: true },
    { text: "Handle one empty host value", done: false },
    { text: "Pass challenge", done: false },
  ],
};

const ide = {
  difficulty: "Beginner",
  estTime: "~12 min",
  starterCode: `hosts = ["10.0.0.1", "", "10.0.0.4"]\nprocessed = 0\n\nfor host in hosts:\n    if host == "":\n        continue\n    print(f"scanning {host}")\n    processed += 1\n\nprint(f"processed={processed}")`,
  stdin: "",
  output: "No output yet. Run code to see logs.",
};

const uiState = {
  loading: false,
  showEmptyOutput: true,
  showToast: true,
  mobileTab: "lesson",
};

export default function App() {
  return <DashboardPage course={courseData} lesson={lesson} ide={ide} uiState={uiState} />;
}
