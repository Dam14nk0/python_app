import React from "react";

export default function AchievementsPage({ language, onPageChange }) {
  return (
    <div className="standalone-page app-shell single">
      <section className="card">
        <div className="top-nav">
          <button className="btn secondary" onClick={() => onPageChange("dashboard")}>Dashboard</button>
          <button className="btn secondary" onClick={() => onPageChange("skill-tree")}>Skill Tree</button>
        </div>
        <h1>{language === "sk" ? "Achievementy" : "Achievements"}</h1>
        <div className="achievements-grid">
          <article className="achievement">🏅 First Challenge Pass</article>
          <article className="achievement">🏅 Checkpoint Conqueror</article>
          <article className="achievement">🏅 Expert Tier Solved</article>
          <article className="achievement">🏅 Capstone Builder</article>
        </div>
      </section>
    </div>
  );
}
