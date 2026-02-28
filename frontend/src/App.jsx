import React, { useMemo, useState } from "react";
import DashboardPage from "./pages/DashboardPage";
import SkillTreePage from "./pages/SkillTreePage";
import AchievementsPage from "./pages/AchievementsPage";
import KaliWorkspacePage from "./pages/KaliWorkspacePage";

const copy = {
  en: {
    pageDashboard: "Dashboard",
    pageSkillTree: "Skill Tree",
    pageAchievements: "Achievements",
    pageKaliWorkspace: "Kali Workspace",
    modeStudy: "Study Mode",
    modeRealWorld: "Real-World Mode",
    lessonTitle: "Why loops exist and how to use them safely",
    intro: "Zero-knowledge friendly lesson with robust loops and error handling.",
    rwScenario: "Scenario: SOC intern processes incoming host list before nightly scan.",
  },
  sk: {
    pageDashboard: "Dashboard",
    pageSkillTree: "Skill strom",
    pageAchievements: "Achievementy",
    pageKaliWorkspace: "Kali Workspace",
    modeStudy: "Študijný režim",
    modeRealWorld: "Reálny režim",
    lessonTitle: "Prečo existujú cykly a ako ich používať bezpečne",
    intro: "Lekcia pre úplných začiatočníkov s dôrazom na bezpečné cykly a ošetrenie chýb.",
    rwScenario: "Scenár: SOC stážista spracúva zoznam hostov pred nočným scanom.",
  },
};

const courseOptions = [
  { track: "Python", slug: "python-for-pentesters", title: "Python for Pentesters" },
  { track: "Bash", slug: "bash-for-pentesters", title: "Bash for Pentesters" },
];

const skillNodesByCourse = {
  "python-for-pentesters": [
    { key: "python-core", name: "Python Core", xp_required: 0, mastery_threshold: 70, related_lessons: [1, 2, 3], deps: [] },
    { key: "automation", name: "Automation", xp_required: 600, mastery_threshold: 70, related_lessons: [15, 16, 17], deps: ["python-core"] },
    { key: "web-interaction", name: "Web Interaction", xp_required: 1300, mastery_threshold: 75, related_lessons: [31, 32, 33], deps: ["automation"] },
    { key: "tool-design", name: "Tool Design", xp_required: 4500, mastery_threshold: 85, related_lessons: [91, 92, 95], deps: ["automation"] },
  ],
  "bash-for-pentesters": [
    { key: "shell-basics", name: "Shell Basics", xp_required: 0, mastery_threshold: 70, related_lessons: [1, 2, 3], deps: [] },
    { key: "pipelines", name: "Pipelines", xp_required: 350, mastery_threshold: 70, related_lessons: [4, 5, 6], deps: ["shell-basics"] },
    { key: "text-processing", name: "Text Processing", xp_required: 700, mastery_threshold: 75, related_lessons: [11, 12, 13], deps: ["pipelines"] },
    { key: "automation", name: "Automation", xp_required: 1200, mastery_threshold: 80, related_lessons: [21, 22, 23], deps: ["text-processing"] },
  ],
};

export default function App() {
  const [language, setLanguage] = useState("en");
  const [mode, setMode] = useState("study");
  const [page, setPage] = useState("dashboard");
  const [courseSlug, setCourseSlug] = useState("python-for-pentesters");
  const t = copy[language];

  const selectedCourse = courseOptions.find((c) => c.slug === courseSlug) || courseOptions[0];

  const course = useMemo(
    () => ({
      category: "Programming",
      track: selectedCourse.track,
      title: selectedCourse.title,
      modules:
        courseSlug === "python-for-pentesters"
          ? [
              { id: "m1", title: "Basics", progress: "3/14", days: [
                { day: 1, title: language === "sk" ? "Čo je Python" : "What is Python", status: "done" },
                { day: 2, title: language === "sk" ? "Premenné a vstup" : "Variables & input", status: "done" },
                { day: 3, title: language === "sk" ? "Prečo sú cykly dôležité" : "Why loops matter", status: "active" },
                { day: 4, title: language === "sk" ? "Funkcie vysvetlené" : "Functions explained", status: "locked" },
              ] },
              { id: "m2", title: "Files & Automation", progress: "0/16", days: [
                { day: 15, title: language === "sk" ? "Bezpečné čítanie súborov" : "Reading files safely", status: "locked" },
                { day: 16, title: language === "sk" ? "Tvorba reportov" : "Writing reports", status: "locked" },
              ] },
            ]
          : [
              { id: "b1", title: "Basics", progress: "2/10", days: [
                { day: 1, title: "Shell basics", status: "done" },
                { day: 2, title: "Variables and quoting", status: "active" },
                { day: 3, title: "Pipes and redirection", status: "locked" },
              ] },
              { id: "b2", title: "Files + Text Processing", progress: "0/10", days: [
                { day: 11, title: "grep/sed/awk intro", status: "locked" },
                { day: 12, title: "Parsing logs with awk", status: "locked" },
              ] },
            ],
    }),
    [courseSlug, language, selectedCourse.title, selectedCourse.track]
  );

  const lesson = {
    day: courseSlug === "python-for-pentesters" ? 3 : 12,
    title: courseSlug === "python-for-pentesters" ? t.lessonTitle : "Bash parsing with grep/sed/awk",
    intro: t.intro,
    realWorldScenario: t.rwScenario,
    isCapstonePart: false,
    kpis: [
      { icon: "⚡", label: "XP", value: "1,240" },
      { icon: "🛡️", label: "Level", value: "Beginner" },
      { icon: "📈", label: "Completion", value: courseSlug === "python-for-pentesters" ? "3%" : "7%" },
      { icon: "🔥", label: "Streak", value: "2 days" },
    ],
    callouts: [
      { type: "idea", title: language === "sk" ? "Čo to je" : "What it is", text: courseSlug === "python-for-pentesters" ? "A loop repeats a block for many targets." : "grep/sed/awk process command output text efficiently." },
      { type: "mistake", title: language === "sk" ? "Častá chyba" : "Common mistake", text: "Assuming every line has identical format." },
      { type: "pro", title: language === "sk" ? "Prečo je to dôležité" : "Why it matters", text: "Real tool outputs are noisy; robust parsing is critical." },
    ],
    steps: ["Load fixture text safely.", "Parse line-by-line with validation.", "Build JSON/CSV output.", "Summarize stats and errors."],
    tasks: [
      { text: "Extract fields from fixture", done: true },
      { text: "Handle malformed lines", done: true },
      { text: "Export structured summary", done: false },
      { text: "Pass challenge", done: false },
    ],
  };

  const ide = {
    difficulty: "Beginner",
    estTime: "~12 min",
    projectMode: lesson.day >= 61,
    activeFile: "main.py",
    openFiles: ["main.py", "modules/scanner.py"],
    fileTree: ["main.py", "modules/scanner.py", "utils/helpers.py", "config.json"],
    starterCode: `hosts = ["10.0.0.1", "", "10.0.0.4"]\nprocessed = 0\nfor host in hosts:\n    if host == "":\n        continue\n    print(host)\n    processed += 1\nprint(processed)`,
    stdin: "",
    output: "No output yet. Run code to see logs.",
    challengeTiers: [
      { name: "Easy", required: true, bonus: "base xp" },
      { name: "Hard", required: false, bonus: "+40 XP" },
      { name: "Expert", required: false, bonus: "badge + XP multiplier" },
    ],
  };

  const uiState = { loading: false, showEmptyOutput: true, showToast: true, mobileTab: "lesson" };

  if (page === "skill-tree") return <SkillTreePage language={language} onPageChange={setPage} nodes={skillNodesByCourse[courseSlug]} />;
  if (page === "achievements") return <AchievementsPage language={language} onPageChange={setPage} />;
  if (page === "kali-workspace") return <KaliWorkspacePage labels={t} onPageChange={setPage} />;

  return (
    <DashboardPage
      course={course}
      lesson={lesson}
      ide={ide}
      uiState={uiState}
      language={language}
      mode={mode}
      labels={t}
      courseSlug={courseSlug}
      courseOptions={courseOptions}
      onCourseChange={setCourseSlug}
      onLanguageChange={setLanguage}
      onModeChange={setMode}
      onPageChange={setPage}
    />
  );
}
