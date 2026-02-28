import React from "react";
import Sidebar from "../components/Sidebar";
import LessonPanel from "../components/LessonPanel";
import IdePanel from "../components/IdePanel";

export default function DashboardPage({
  course,
  lesson,
  ide,
  uiState,
  language,
  mode,
  labels,
  courseSlug,
  courseOptions,
  onCourseChange,
  onLanguageChange,
  onModeChange,
  onPageChange,
}) {
  return (
    <div className="app-shell">
      <header className="top-toolbar card">
        <div className="toolbar-left">
          <button className="btn secondary" onClick={() => onPageChange("dashboard")}>{labels.pageDashboard}</button>
          <button className="btn secondary" onClick={() => onPageChange("skill-tree")}>{labels.pageSkillTree}</button>
          <button className="btn secondary" onClick={() => onPageChange("achievements")}>{labels.pageAchievements}</button>
          <button className="btn secondary" onClick={() => onPageChange("kali-workspace")}>{labels.pageKaliWorkspace}</button>
        </div>
        <div className="toolbar-right">
          <select value={courseSlug} onChange={(e) => onCourseChange(e.target.value)}>
            {courseOptions.map((courseItem) => (
              <option key={courseItem.slug} value={courseItem.slug}>{courseItem.track} → {courseItem.title}</option>
            ))}
          </select>
          <select value={language} onChange={(e) => onLanguageChange(e.target.value)}>
            <option value="en">EN</option>
            <option value="sk">SK</option>
            <option value="cz">CZ</option>
          </select>
          <button className={`btn ${mode === "study" ? "primary" : "secondary"}`} onClick={() => onModeChange("study")}>{labels.modeStudy}</button>
          <button className={`btn ${mode === "real-world" ? "primary" : "secondary"}`} onClick={() => onModeChange("real-world")}>{labels.modeRealWorld}</button>
        </div>
      </header>

      <header className="mobile-tabs card">
        <button className={`tab-btn ${uiState.mobileTab === "lesson" ? "active" : ""}`}>Lesson</button>
        <button className={`tab-btn ${uiState.mobileTab === "ide" ? "active" : ""}`}>IDE</button>
      </header>

      <Sidebar course={course} />
      <LessonPanel lesson={lesson} loading={uiState.loading} mode={mode} />
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
