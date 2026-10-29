<script lang="ts">
  import { AtIcon, GithubLogoIcon, LinkedinLogoIcon } from "phosphor-svelte";
  import { CONTACTS } from "$lib/constants/contact";
  import { techLogos } from "./tech-logos";
  import EncryptedText from "../reusable/encrypted-text.svelte";

  let sceneReady = $state(false);

  function mountScene(canvas: HTMLCanvasElement) {
    let disposed = false;
    let cleanup: (() => void) | undefined;

    void import("./tech-logo-scene")
      .then(({ createTechLogoScene }) => {
        if (disposed) return;

        cleanup = createTechLogoScene(canvas);
        sceneReady = true;
      })
      .catch(() => {
        sceneReady = false;
      });

    return () => {
      disposed = true;
      cleanup?.();
    };
  }
</script>

<section class="sticky top-0 isolate h-svh min-h-140 overflow-clip bg-white">
  <div class="pointer-events-none absolute inset-0 h-full w-full">
    <canvas
      {@attach mountScene}
      aria-hidden="true"
      class="absolute inset-0 h-full w-full"
      class:opacity-0={!sceneReady}
      class:opacity-100={sceneReady}
    ></canvas>
    <ul
      class="absolute inset-0 m-0 h-full w-full list-none p-0"
      class:opacity-0={sceneReady}
      aria-label="Technologies I work with"
    >
      {#each techLogos as technology (technology.file)}
        <li
          class="absolute top-(--y) left-(--x) w-(--size) transform-[translate(-50%,-50%)_rotate(var(--rotation))] max-md:w-[calc(var(--size)*0.5)] max-md:top-(--mobile-y) max-md:left-(--mobile-x)"
          class:max-md:invisible={!technology.mobileVisible}
          style:--x={`${technology.desktopPosition.x}%`}
          style:--y={`${technology.desktopPosition.y}%`}
          style:--mobile-x={`${technology.mobilePosition.x}%`}
          style:--mobile-y={`${technology.mobilePosition.y}%`}
          style:--size={`${technology.size}px`}
          style:--rotation={`${-technology.rz}rad`}
        >
          <img
            class="block h-auto w-full filter-[drop-shadow(4px_8px_5px_rgb(0_0_0/0.15))]"
            src={`/assets/tech-stack/${technology.file}.svg`}
            alt={technology.name}
            width="96"
            height="96"
          />
        </li>
      {/each}
    </ul>
  </div>

  <div
    class="relative z-1 mx-auto flex flex-col gap-4 h-[72%] w-[68%] items-center justify-center max-md:h-[76%] max-md:w-[72%]"
  >
    <h1
      class="text-center font-writer text-5xl leading-[1.08] font-bold text-black md:text-8xl"
    >
      Agnostic
      <EncryptedText texts={["Framework", "AI Tools"]} interval={3000} /><br />
      Programmer
    </h1>
    <p class="text-black/60 md:text-xl text-sm max-w-1/2 md:w-full text-center">
      Building software since AI were still stupid
    </p>

    <!-- Contact -->
    <div class="flex items-center">
      {#each CONTACTS as contact (contact.label)}
        {#if contact.href}
          <a
            href={contact.href}
            aria-label={contact.label}
            title={contact.label}
            class="inline-flex size-11 items-center justify-center rounded-full text-black focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-black"
          >
            {#if contact.label === "GitHub"}
              <GithubLogoIcon weight="fill" size={28} aria-hidden="true" />
            {:else if contact.label === "LinkedIn"}
              <LinkedinLogoIcon weight="fill" size={28} aria-hidden="true" />
            {:else if contact.label === "Email"}
              <AtIcon weight="fill" size={28} aria-hidden="true" />
            {/if}
          </a>
        {/if}
      {/each}
    </div>
  </div>

  <img
    src="/assets/avatar/adics-head.png"
    alt="Adi looking up at the technologies"
    class="absolute bottom-0 left-1/2 z-[1] w-[min(50vw,640px)] -translate-x-1/2 max-md:w-[min(100%,640px)]"
  />
</section>
