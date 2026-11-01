import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export function scrollYears(node: HTMLElement) {
  gsap.registerPlugin(ScrollTrigger);

  const media = gsap.matchMedia();
  let disposed = false;

  media.add(
    "(min-width: 900px) and (min-height: 700px) and (prefers-reduced-motion: no-preference)",
    () => {
      const deck = node.querySelector<HTMLElement>("[data-year-deck]");
      if (!deck) return;

      const sheets = Array.from(node.querySelectorAll<HTMLElement>("[data-year-sheet]"));

      gsap.set(node, { height: "100vh" });
      gsap.set(deck, {
        flex: 1,
        minHeight: 0,
        flexDirection: "row",
      });
      gsap.set(sheets, {
        width: "min(420px, 50vh)",
        flexShrink: 0,
        minHeight: 0,
      });

      const travel = () => Math.max(0, deck.scrollWidth - deck.clientWidth);
      let animation: gsap.Context | undefined;
      let hasOverflow = false;

      function updateOverflow() {
        const nextHasOverflow = travel() > 1;
        if (nextHasOverflow === hasOverflow) return;

        hasOverflow = nextHasOverflow;
        animation?.revert();
        animation = undefined;

        if (hasOverflow) {
          animation = gsap.context(() => {
            gsap.to(deck, {
              x: () => -travel(),
              ease: "none",
              scrollTrigger: {
                trigger: node,
                start: "top top",
                end: () => `+=${travel()}`,
                pin: true,
                scrub: 0.6,
                invalidateOnRefresh: true,
              },
            });
          }, node);
        }

        ScrollTrigger.refresh();
      }

      updateOverflow();

      const observer = new ResizeObserver(updateOverflow);
      observer.observe(deck);

      return () => {
        observer.disconnect();
        animation?.revert();
      };
    },
  );

  void document.fonts.ready.then(() => {
    if (!disposed) ScrollTrigger.refresh();
  });

  return () => {
    disposed = true;
    media.revert();
  };
}
