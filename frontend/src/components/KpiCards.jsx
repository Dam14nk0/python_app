import React from "react";
export default function KpiCards({ items, loading }) {
  return (
    <section className="kpi-grid">
      {items.map((item) => (
        <article className="kpi" key={item.label}>
          {loading ? (
            <div className="skeleton skeleton-kpi" />
          ) : (
            <>
              <p className="kpi-label">
                <span>{item.icon}</span>
                {item.label}
              </p>
              <p className="kpi-value">{item.value}</p>
            </>
          )}
        </article>
      ))}
    </section>
  );
}
