export const startLoopSection = () => {
  const root = document.getElementById("main");
  if (!root) return;

  const sectionIds = ["home", "work", "stack", "experience"];
  const sections = Array.from(root?.children).filter((child) =>
    sectionIds.includes(child.id),
  );

  const lastSectionIdx = sections.length - 1;

  // Cut all section but preserve the last one, then append at the end
  sections.forEach((section, idx) => {
    if (idx !== lastSectionIdx) {
      root.removeChild(section);

      if (idx !== 0) {
        root.appendChild(section);
      }
    }
  });
};
