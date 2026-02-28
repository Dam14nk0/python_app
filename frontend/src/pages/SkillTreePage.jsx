import React from "react";

export default function SkillTreePage({ language, onPageChange, nodes }) {
  const title = language === "sk" ? "Skill strom" : "Skill Tree";
  return (
    <div className="standalone-page app-shell single">
      <section className="card">
        <div className="top-nav">
          <button className="btn secondary" onClick={() => onPageChange("dashboard")}>Dashboard</button>
          <button className="btn secondary" onClick={() => onPageChange("achievements")}>Achievements</button>
        </div>
        <h1>{title}</h1>
        <div className="skill-tree-grid">
          {nodes.map((node) => (
            <article className="skill-node" key={node.key}>
              <h3>{node.name}</h3>
              <p>XP: {node.xp_required}</p>
              <p>Mastery target: {node.mastery_threshold}%</p>
              <p>Lessons: {node.related_lessons.join(", ")}</p>
              <p>Dependencies: {node.deps.length ? node.deps.join(", ") : "None"}</p>
              <div className="mastery-bar"><span style={{ width: `${Math.min(100, Math.floor(node.related_lessons.length * 20))}%` }} /></div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}
