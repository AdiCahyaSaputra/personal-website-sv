import { ScrollTrigger } from "gsap/ScrollTrigger";
import { isHomeIntersect } from "$lib/state/is-home-intersect.svelte";

export const startLoopSection = (root: HTMLElement) => {
  const originalHome = root.querySelector<HTMLElement>(":scope > #home");
  const originalEnd = root.querySelector<HTMLElement>(":scope > #home-loop");
  if (!originalHome || !originalEnd) return;

  const homeNextSibling = originalHome.nextSibling;
  const endNextSibling = originalEnd.nextSibling;
  const overflowAnchor = root.style.overflowAnchor;

  let home = originalHome;
  let end = originalEnd;

  let frame = 0;

  root.style.overflowAnchor = "none";

  function update() {
    if (frame) return;

    const homeBounds = home.getBoundingClientRect();
    const endBounds = end.getBoundingClientRect();

    const homeIsVisible =
      homeBounds.top >= -1 && homeBounds.bottom <= window.innerHeight + 1;
    const endIsVisible =
      endBounds.top >= -1 && endBounds.bottom <= window.innerHeight + 1;

    isHomeIntersect.value = homeIsVisible || endIsVisible;

    if (endBounds.top > 1) return;

    // Keep the visible Home instance, preserving its running text animation.
    root.insertBefore(end, home);
    root.insertBefore(home, endNextSibling);

    home.id = "home-loop";
    end.id = "home";

    // Swap it
    [home, end] = [end, home];

    function restorePosition() {
      // Why do we need to swap two home when eventually did this ? to preserve the current text animation so the changes is'nt noticable
      window.scrollTo({
        top: window.scrollY + home.getBoundingClientRect().top - endBounds.top,
        behavior: "instant",
      });
    }

    frame = requestAnimationFrame(() => {
      frame = 0;
    });

    restorePosition();
    ScrollTrigger.refresh();
    restorePosition();
    ScrollTrigger.update();
  }

  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();

  return () => {
    window.removeEventListener("scroll", update);
    window.removeEventListener("resize", update);
    cancelAnimationFrame(frame);

    // Restore Svelte's original node order before the page is torn down.
    root.insertBefore(originalHome, homeNextSibling);
    root.insertBefore(originalEnd, endNextSibling);

    originalHome.id = "home";
    originalEnd.id = "home-loop";

    root.style.overflowAnchor = overflowAnchor;

    isHomeIntersect.value = false;
  };
};
