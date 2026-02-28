import React from "react";
import Sidebar from "../components/Sidebar";
import LessonPanel from "../components/LessonPanel";
import IdePanel from "../components/IdePanel";

export default function DashboardPage({ course, lesson, ide, uiState }) {
  return (
    <div className="app-shell">
      <header className="mobile-tabs card">
        <button className={`tab-btn ${uiState.mobileTab === "lesson" ? "active" : ""}`}>Lesson</button>
        <button className={`tab-btn ${uiState.mobileTab === "ide" ? "active" : ""}`}>IDE</button>
      </header>

      <Sidebar course={course} />
      <LessonPanel lesson={lesson} loading={uiState.loading} />
      <IdePanel ide={ide} loading={uiState.loading} showEmptyOutput={uiState.showEmptyOutput} />

      {uiState.showToast && (
        <div className="toast-stack">
          <div className="toast success">✅ Progress saved • +10 XP</div>
          <div className="toast info">ℹ️ Tip: Ctrl + Enter to Run</div>
        </div>
      )}
    </div>
  );
}
