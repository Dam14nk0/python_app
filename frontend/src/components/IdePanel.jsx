import React from "react";

export default function IdePanel({ ide, loading, showEmptyOutput }) {
  return (
    <aside className="ide-panel card">
      <header className="challenge-header">
        <div>
          <p className="eyebrow">Challenge</p>
          <h2>Build resilient loop logic</h2>
          {ide.projectMode ? <span className="badge persistence">Project Mode</span> : null}
        </div>
        <div className="badges">
          <span className="badge difficulty">{ide.difficulty}</span>
          <span className="badge time">{ide.estTime}</span>
        </div>
      </header>

      <section className="tier-box card-soft">
        <p className="section-title">Challenge tiers</p>
        <ul className="tier-list">
          {ide.challengeTiers.map((tier) => (
            <li key={tier.name}>
              <strong>{tier.name}</strong> {tier.required ? "(required)" : "(optional)"} · {tier.bonus}
            </li>
          ))}
        </ul>
      </section>

      <section className="editor-shell card-soft">
        <aside className="file-tree">
          <p className="section-title">Files</p>
          <ul>
            {ide.fileTree.map((file) => (
              <li key={file} className={file === ide.activeFile ? "active" : ""}>{file}</li>
            ))}
          </ul>
        </aside>

        <div className="editor-main">
          <div className="file-tabs">
            {ide.openFiles.map((file) => (
              <span key={file} className={file === ide.activeFile ? "tab active" : "tab"}>{file}</span>
            ))}
          </div>
          <section className="editor card-soft">
            <p className="section-title">Code editor</p>
            {loading ? <div className="skeleton skeleton-editor" /> : <pre>{ide.starterCode}</pre>}
          </section>
        </div>
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
