import React from "react";

export default function Sidebar({ course }) {
  const dot = (status) => {
    if (status === "done") return "dot done";
    if (status === "active") return "dot active";
    return "dot";
  };

  return (
    <aside className="sidebar card">
      <div className="course-head">
        <p className="eyebrow">{course.category} / {course.track}</p>
        <h2>{course.title}</h2>
      </div>

      {course.modules.map((module) => (
        <section className="module-card" key={module.id}>
          <div className="module-top">
            <h3>{module.title}</h3>
            <span>{module.progress}</span>
          </div>

          <ul className="day-list">
            {module.days.map((item) => (
              <li className={`day-row ${item.status}`} key={`${module.id}-${item.day}`}>
                <span className={dot(item.status)} />
                <span className="day-text">Day {item.day}: {item.title}</span>
                {item.status === "locked" ? <span className="lock">🔒</span> : null}
              </li>
            ))}
          </ul>
        </section>
      ))}
    </aside>
  );
}
