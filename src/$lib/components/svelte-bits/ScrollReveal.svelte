<script module lang="ts">
  import { gsap } from "gsap";
  import { ScrollTrigger } from "gsap/ScrollTrigger";

  gsap.registerPlugin(ScrollTrigger);
</script>

<script lang="ts">
  type Props = {
    text: string;
    scrollContainer?: HTMLElement | null;
    enableBlur?: boolean;
    baseOpacity?: number;
    baseRotation?: number;
    blurStrength?: number;
    containerClassName?: string;
    textClassName?: string;
    rotationEnd?: string;
    wordAnimationStart?: string;
    wordAnimationEnd?: string;
    scrub?: number | boolean;
  };

  let {
    text,
    scrollContainer = null,
    enableBlur = true,
    baseOpacity = 0.1,
    baseRotation = 3,
    blurStrength = 4,
    containerClassName = "",
    textClassName = "",
    rotationEnd = "bottom bottom",
    wordAnimationStart = "top center",
    wordAnimationEnd = "bottom 20%",
    scrub = 0.8,
  }: Props = $props();

  let containerEl: HTMLHeadingElement | undefined = $state();

  const splitParts = $derived(text.split(/(\s+)/));

  $effect(() => {
    const el = containerEl;
    if (!el) return;

    void enableBlur;
    void baseOpacity;
    void baseRotation;
    void blurStrength;
    void rotationEnd;
    void wordAnimationStart;
    void wordAnimationEnd;
    void scrub;
    void scrollContainer;
    void splitParts;

    const scroller = scrollContainer ?? window;
    const triggers: ScrollTrigger[] = [];

    const rotationTween = gsap.fromTo(
      el,
      { transformOrigin: "0% 50%", rotate: baseRotation },
      {
        ease: "none",
        rotate: 0,
        scrollTrigger: {
          trigger: el,
          scroller,
          start: "top bottom",
          end: rotationEnd,
          scrub,
        },
      },
    );
    if (rotationTween.scrollTrigger) triggers.push(rotationTween.scrollTrigger);

    const wordElements = el.querySelectorAll(".scroll-reveal-word");

    const opacityTween = gsap.fromTo(
      wordElements,
      { opacity: baseOpacity, willChange: "opacity" },
      {
        ease: "none",
        opacity: 1,
        stagger: 0.5,
        scrollTrigger: {
          trigger: el,
          scroller,
          start: wordAnimationStart,
          end: wordAnimationEnd,
          scrub,
        },
      },
    );
    if (opacityTween.scrollTrigger) triggers.push(opacityTween.scrollTrigger);

    if (enableBlur) {
      const blurTween = gsap.fromTo(
        wordElements,
        { filter: `blur(${blurStrength}px)` },
        {
          ease: "none",
          filter: "blur(0px)",
          stagger: 0.5,
          scrollTrigger: {
            trigger: el,
            scroller,
            start: wordAnimationStart,
            end: wordAnimationEnd,
            scrub,
          },
        },
      );
      if (blurTween.scrollTrigger) triggers.push(blurTween.scrollTrigger);
    }

    return () => {
      triggers.forEach((t) => t.kill());
    };
  });
</script>

<h2 bind:this={containerEl} class="scroll-reveal {containerClassName}">
  <p class="scroll-reveal-text {textClassName}">
    {#each splitParts as part, i (i)}
      {#if /^\s+$/.test(part)}{part}{:else}<span class="scroll-reveal-word"
          >{part}</span
        >{/if}
    {/each}
  </p>
</h2>

<style>
  .scroll-reveal {
    margin: 0;
  }

  .scroll-reveal-text {
    font-size: clamp(1.6rem, 4vw, 3rem);
    line-height: 1.5;
    font-weight: 600;
  }

  .scroll-reveal-word {
    display: inline-block;
  }
</style>
