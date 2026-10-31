import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

export function stackCards(node: HTMLElement) {
  gsap.registerPlugin(ScrollTrigger);

  const media = gsap.matchMedia();
  let disposed = false;

  media.add(
    "(min-width: 900px) and (min-height: 700px) and (prefers-reduced-motion: no-preference)",
    () => {
      const cards = Array.from(
        node.querySelectorAll<HTMLElement>("[data-stack-card]"),
      );

      const initialTopOffset = 108;

      cards.forEach((card, index) => {
        const next = cards[index + 1];
        const panel = card.querySelector<HTMLElement>("[data-card-panel]");

        ScrollTrigger.create({
          trigger: card,
          start: () => `top ${initialTopOffset + index * 56}px`,
          endTrigger: "#work",
          end: () => {
            const stackBottom = initialTopOffset + cards[index].offsetHeight;

            return `clamp(bottom ${stackBottom}px)`;
          },
          pin: true,
          pinSpacing: false,
          invalidateOnRefresh: true,
        });

        if (next && panel) {
          gsap.to(panel, {
            scale: 1 - cards.length / 100 + index / 100, // len = 3, so it start 0.97, 0.98, 0.99
            transformOrigin: "50% 0%",
            ease: "none",
            scrollTrigger: {
              trigger: next,
              start: "top 85%",
              end: () => `top ${initialTopOffset + (index + 1) * 56}px`,
              scrub: true,
              invalidateOnRefresh: true,
            },
          });
        }
      });
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

export function progressingTitle(node: HTMLElement) {
  gsap.registerPlugin(ScrollTrigger);

  gsap.fromTo(
    node,
    { x: () => window.innerWidth }, // far right
    {
      x: () => 0, // far left
      ease: "none",
      scrollTrigger: {
        trigger: node,
        start: "center bottom",
        end: "center 20%",
        scrub: true,
        invalidateOnRefresh: true,
      },
    },
  );
}
