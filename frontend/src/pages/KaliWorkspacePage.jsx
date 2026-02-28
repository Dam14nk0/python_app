import React, { useMemo, useState } from "react";

const defaultFiles = [
  { path: "outputs/nmap.txt", content: "" },
  { path: "outputs/ffuf.txt", content: "" },
  { path: "outputs/report.md", content: "# Report\n" },
];

export default function KaliWorkspacePage({ labels, onPageChange }) {
  const [files, setFiles] = useState(defaultFiles);
  const [activePath, setActivePath] = useState(defaultFiles[0].path);
  const [search, setSearch] = useState("");

  const outputBlocks = [
    { name: "nmap_basic_scan", content: "Nmap scan report for 10.10.10.10\n22/tcp open ssh\n80/tcp open http\n" },
    { name: "ffuf_api_probe", content: "admin [Status: 301, Size: 0]\napi [Status: 200, Size: 1234]\n" },
    { name: "gobuster_dirs", content: "[+] Url: /admin (Status: 301)\n[+] Url: /login (Status: 200)\n" },
  ];

  const filteredBlocks = useMemo(
    () => outputBlocks.filter((block) => block.content.toLowerCase().includes(search.toLowerCase()) || block.name.toLowerCase().includes(search.toLowerCase())),
    [search]
  );

  const activeFile = files.find((file) => file.path === activePath) || files[0];

  function updateFileContent(content) {
    setFiles((prev) => prev.map((file) => (file.path === activePath ? { ...file, content } : file)));
  }

  function createFile() {
    const path = window.prompt("New file path", "outputs/new.txt");
    if (!path) return;
    if (files.some((f) => f.path === path)) return;
    setFiles((prev) => [...prev, { path, content: "" }]);
    setActivePath(path);
  }

  function saveBlockToFile(block) {
    const path = window.prompt("Save block to file", "outputs/input.txt");
    if (!path) return;
    const existing = files.find((file) => file.path === path);
    if (existing) {
      setFiles((prev) => prev.map((file) => (file.path === path ? { ...file, content: block.content } : file)));
    } else {
      setFiles((prev) => [...prev, { path, content: block.content }]);
    }
    setActivePath(path);
  }

  function resetWorkspace() {
    setFiles(defaultFiles);
    setActivePath(defaultFiles[0].path);
  }

  return (
    <div className="app-shell">
      <header className="top-toolbar card">
        <div className="toolbar-left">
          <button className="btn secondary" onClick={() => onPageChange("dashboard")}>{labels.pageDashboard}</button>
          <button className="btn secondary" onClick={() => onPageChange("kali-workspace")}>{labels.pageKaliWorkspace}</button>
        </div>
        <div className="toolbar-right">
          <button className="btn secondary" onClick={createFile}>New file</button>
          <button className="btn secondary" onClick={resetWorkspace}>Reset workspace</button>
        </div>
      </header>

      <section className="kali-layout">
        <aside className="card kali-pane">
          <h3>File Explorer</h3>
          <div className="file-list">
            {files.map((file) => (
              <button key={file.path} className={`file-item ${file.path === activePath ? "active" : ""}`} onClick={() => setActivePath(file.path)}>{file.path}</button>
            ))}
          </div>
          <textarea value={activeFile?.content || ""} onChange={(e) => updateFileContent(e.target.value)} rows={12} />
        </aside>

        <main className="card kali-pane">
          <h3>Terminal Output Viewer</h3>
          <input placeholder="Search output..." value={search} onChange={(e) => setSearch(e.target.value)} />
          <div className="output-blocks">
            {filteredBlocks.map((block) => (
              <article key={block.name} className="output-block">
                <div className="output-block-header">
                  <strong>{block.name}</strong>
                  <div>
                    <button className="btn secondary" onClick={() => navigator.clipboard.writeText(block.content)}>Copy block</button>
                    <button className="btn primary" onClick={() => saveBlockToFile(block)}>Save to file...</button>
                  </div>
                </div>
                <pre>{block.content}</pre>
              </article>
            ))}
          </div>
        </main>

        <aside className="card kali-pane">
          <h3>Notes / Tasks</h3>
          <ul>
            <li>Save the nmap output to outputs/nmap.txt</li>
            <li>Save the ffuf output to outputs/ffuf.txt</li>
            <li>Extract open ports into outputs/ports.json</li>
            <li>Parse ffuf results into outputs/endpoints.csv</li>
            <li>Write summary into outputs/report.md</li>
          </ul>
          <p><strong>Required files:</strong> outputs/nmap.txt, outputs/ffuf.txt, outputs/ports.json, outputs/endpoints.csv</p>
        </aside>
      </section>
    </div>
  );
}
