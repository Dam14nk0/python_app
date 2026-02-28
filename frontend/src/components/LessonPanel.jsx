import React from "react";
import KpiCards from "./KpiCards";

export default function LessonPanel({ lesson, loading }) {
  const doneCount = lesson.tasks.filter((task) => task.done).length;

  return (
    <main className="lesson-panel card">
      <div className="lesson-header">
        <div>
          <p className="eyebrow">Dashboard</p>
          <h1>{lesson.title}</h1>
        </div>
        <button className="cta-btn">Continue Day {lesson.day}</button>
      </div>

      <KpiCards items={lesson.kpis} loading={loading} />

      <section className="lesson-content card-soft">
        {loading ? <div className="skeleton skeleton-line" /> : <p>{lesson.intro}</p>}

        <div className="lesson-actions">
          <button className="btn secondary">View notes</button>
          <button className="btn secondary">Download template</button>
          <button className="btn primary">Mark lesson in progress</button>
        </div>

        <div className="callout-grid">
          {lesson.callouts.map((callout) => (
            <article className={`callout ${callout.type}`} key={callout.title}>
              <h4>{callout.title}</h4>
              <p>{callout.text}</p>
            </article>
          ))}
        </div>

        <div className="steps-wrap">
          <h3>Step-by-step path</h3>
          <ol className="steps-list">
            {lesson.steps.map((step, index) => (
              <li key={step}>
                <span className="step-index">{index + 1}</span>
                <span className="step-text">{step}</span>
              </li>
            ))}
          </ol>
        </div>

        <div className="tasks-wrap">
          <div className="tasks-head">
            <h3>Tasks checklist</h3>
            <span>{doneCount}/{lesson.tasks.length}</span>
          </div>
          <ul className="task-list">
            {lesson.tasks.map((task) => (
              <li key={task.text} className={task.done ? "done" : ""}>
                <span>{task.done ? "✅" : "⬜"}</span>
                {task.text}
              </li>
            ))}
          </ul>
        </div>
      </section>
    </main>
  );
}
