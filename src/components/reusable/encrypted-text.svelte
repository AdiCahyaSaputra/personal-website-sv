<script lang="ts">
  type Props = {
    texts: readonly string[];
    interval?: number;
    duration?: number;
    characters?: string;
    class?: string;
  };

  let {
    texts,
    interval = 2000,
    duration = 600,
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*",
    class: className = "",
  }: Props = $props();

  let animatedText = $state<string | null>(null);
  const displayedText = $derived(animatedText ?? texts[0] ?? "");

  $effect(() => {
    const words = [...texts];
    const delay = Math.max(1, interval);
    const transitionDuration = Math.min(Math.max(0, duration), delay);
    const alphabet = Array.from(characters || "ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    let index = 0;
    let frame = 0;

    animatedText = words[0] ?? "";

    if (words.length < 2) return;

    const timer = window.setInterval(() => {
      cancelAnimationFrame(frame);
      index = (index + 1) % words.length;

      const target = words[index] ?? "";

      if (reducedMotion.matches || transitionDuration === 0) {
        animatedText = target;
        return;
      }

      const letters = Array.from(target);
      const startedAt = performance.now();
      let lastStep = -1;

      function animate(now: number) {
        const elapsed = now - startedAt;
        const progress = Math.min(elapsed / transitionDuration, 1);
        const step = Math.floor(elapsed / 40);

        if (progress === 1) {
          animatedText = target;
          return;
        }

        if (step !== lastStep) {
          const revealed = Math.floor(progress * letters.length);

          animatedText = letters
            .map((letter, position) => {
              if (position < revealed || /\s/.test(letter)) return letter;

              return alphabet[Math.floor(Math.random() * alphabet.length)] ?? letter;
            })
            .join("");
          lastStep = step;
        }

        frame = requestAnimationFrame(animate);
      }

      frame = requestAnimationFrame(animate);
    }, delay);

    return () => {
      window.clearInterval(timer);
      cancelAnimationFrame(frame);
    };
  });
</script>

<span class={`encrypted-text ${className}`}>
  <span class="sr-only">{texts.join(", ")}</span>
  <span class="visible-text" aria-hidden="true">{displayedText}</span>
</span>

<style>
  .encrypted-text {
    display: inline-block;
  }

  .visible-text {
    white-space: pre;
  }
</style>
