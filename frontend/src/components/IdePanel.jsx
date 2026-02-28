import React from "react";
export default function IdePanel({ ide, loading, showEmptyOutput }) {
  return (
    <aside className="ide-panel card">
      <header className="challenge-header">
        <div>
          <p className="eyebrow">Challenge</p>
          <h2>Build resilient loop logic</h2>
        </div>
        <div className="badges">
          <span className="badge difficulty">{ide.difficulty}</span>
          <span className="badge time">{ide.estTime}</span>
        </div>
      </header>

      <section className="editor card-soft">
        <p className="section-title">Code editor</p>
        {loading ? <div className="skeleton skeleton-editor" /> : <pre>{ide.starterCode}</pre>}
      </section>

      <section className="stdin card-soft">
        <p className="section-title">STDIN</p>
        <div className="input-box">{ide.stdin || "(empty)"}</div>
      </section>

      <div className="action-row">
        <button className="btn primary">Run</button>
        <button className="btn secondary">Check</button>
      </div>
      <div className="action-row tertiary">
        <button className="btn ghost">Reset code</button>
        <button className="btn ghost">Show hint</button>
      </div>

      <section className="output-card">
        <p className="section-title">Output</p>
        {showEmptyOutput ? <p className="empty-state">No output yet. Click Run to execute code.</p> : <pre>{ide.output}</pre>}
      </section>
    </aside>
  );
}
