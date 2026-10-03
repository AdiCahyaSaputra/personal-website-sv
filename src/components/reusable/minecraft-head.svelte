<script lang="ts">
  import { gsap } from "gsap";

  // Hair masks follow the original skin's 8 × 8 pixel boundaries.
  const faces = [
    {
      name: "front", x: 8, y: 8, transform: "translateZ(14px)", shade: 0,
      hairMask: "polygon(0 0, 100% 0, 100% 75%, 87.5% 75%, 87.5% 50%, 75% 50%, 75% 37.5%, 62.5% 37.5%, 62.5% 62.5%, 50% 62.5%, 50% 50%, 37.5% 50%, 37.5% 37.5%, 25% 37.5%, 25% 50%, 12.5% 50%, 12.5% 75%, 0 75%)",
    },
    {
      name: "right", x: 16, y: 8, transform: "rotateY(90deg) translateZ(14px)", shade: 0.2,
      hairMask: "polygon(0 0, 100% 0, 100% 100%, 25% 100%, 25% 87.5%, 12.5% 87.5%, 12.5% 75%, 0 75%)",
    },
    {
      name: "back", x: 24, y: 8, transform: "rotateY(180deg) translateZ(14px)", shade: 0.25,
      hairMask: "inset(0)",
    },
    {
      name: "left", x: 0, y: 8, transform: "rotateY(-90deg) translateZ(14px)", shade: 0.15,
      hairMask: "polygon(0 0, 100% 0, 100% 75%, 87.5% 75%, 87.5% 87.5%, 75% 87.5%, 75% 100%, 0 100%)",
    },
    {
      name: "top", x: 8, y: 0, transform: "rotateX(90deg) translateZ(14px)", shade: 0.05,
      hairMask: "inset(0)",
    },
    {
      name: "bottom", x: 16, y: 0, transform: "rotateX(-90deg) translateZ(14px)", shade: 0.3,
      hairMask: null,
    },
  ];

  function trackPointer(element: HTMLElement) {
    const media = gsap.matchMedia();
    media.add("(min-width: 768px) and (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference)", () => {
      const pose = { pitch: -10, yaw: -18 };
      const render = () => {
        element.style.transform = `rotateX(${pose.pitch}deg) rotateY(${pose.yaw}deg)`;
      };
      render();

      function move(event: PointerEvent) {
        if (event.pointerType !== "mouse" || !element.checkVisibility()) return;
        const bounds = element.getBoundingClientRect();
        const x = gsap.utils.clamp(-1, 1, (event.clientX - bounds.left - bounds.width / 2) / (window.innerWidth / 2));
        const y = gsap.utils.clamp(-1, 1, (event.clientY - bounds.top - bounds.height / 2) / (window.innerHeight / 2));
        gsap.to(pose, {
          pitch: -y * 14,
          yaw: x * 22,
          duration: 0.3,
          ease: "power2.out",
          overwrite: true,
          onUpdate: render,
        });
      }

      function reset() {
        gsap.to(pose, {
          pitch: -10, yaw: -18,
          duration: 0.4, ease: "power2.out", overwrite: true, onUpdate: render,
        });
      }

      window.addEventListener("pointermove", move, { passive: true });
      document.documentElement.addEventListener("pointerleave", reset);
      window.addEventListener("blur", reset);

      return () => {
        window.removeEventListener("pointermove", move);
        document.documentElement.removeEventListener("pointerleave", reset);
        window.removeEventListener("blur", reset);
        gsap.killTweensOf(pose);
        element.style.removeProperty("transform");
      };
    });
    return () => media.revert();
  }
</script>

<span class="relative block size-11 perspective-[240px]" aria-hidden="true">
  <span class="absolute inset-0 m-auto block size-[28px] transform-3d" data-minecraft-head {@attach trackPointer}>
    {#each faces as face (face.name)}
      <span
        class="absolute inset-0 block size-[28px] bg-[url('/assets/avatar/minecraft-skin.png')] bg-size-[224px_224px] bg-no-repeat [image-rendering:pixelated] backface-hidden after:pointer-events-none after:absolute after:inset-0 after:bg-black after:opacity-(--shade)"
        style:background-position={`${-face.x * 3.5}px ${-face.y * 3.5}px`}
        style:transform={face.transform}
        style:--shade={face.shade}
      >
        {#if face.hairMask}
          <span class="absolute inset-0 block bg-black" style:clip-path={face.hairMask}></span>
        {/if}
      </span>
    {/each}
  </span>
</span>
