<script lang="ts">
  import { TECH_STACKS } from "$lib/constants/skill";
  import EncryptedText from "../reusable/encrypted-text.svelte";

  const groups = [
    ...new Map(
      TECH_STACKS.map((skill) => [
        skill.group,
        { name: skill.group, style: skill.groupStyle },
      ]),
    ).values(),
  ];

  let isLegendFloating = $state(false);
  let legendHeight = $state(0);

  function measureLegend(node: HTMLElement) {
    function measure() {
      if (isLegendFloating) return;

      const style = getComputedStyle(node);
      legendHeight = node.offsetHeight + parseFloat(style.marginTop);
    }

    measure();

    const resizeObserver = new ResizeObserver(measure);
    resizeObserver.observe(node);

    return {
      destroy() {
        resizeObserver.disconnect();
      },
    };
  }

  function observeSection(node: HTMLElement) {
    function updatePosition() {
      const bounds = node.getBoundingClientRect();
      const viewportBottom = window.innerHeight;

      isLegendFloating =
        bounds.top < viewportBottom && bounds.bottom > viewportBottom;

      if (!isLegendFloating) {
        hoveredGroup = null;
      }
    }

    function onScrollOrResize() {
      window.addEventListener("scroll", updatePosition, { passive: true });
      window.addEventListener("resize", updatePosition);
    }

    const frame = requestAnimationFrame(updatePosition);
    const resizeObserver = new ResizeObserver(updatePosition);
    resizeObserver.observe(node);

    onScrollOrResize();

    return {
      destroy() {
        cancelAnimationFrame(frame);
        resizeObserver.disconnect();

        onScrollOrResize();
      },
    };
  }

  let selectedGroup = $state<string | null>(null);
  let hoveredGroup = $state<string | null>(null);

  const activeGroups = $derived(
    new Set([selectedGroup, hoveredGroup].filter((group) => group !== null)),
  );
</script>

<svelte:window
  onkeydown={(event) => {
    if (event.key === "Escape") {
      selectedGroup = null;
      hoveredGroup = null;
    }
  }}
/>

<section id="stack" class="mt-32 p-4 md:p-10" use:observeSection>
  <div class="flex justify-between items-start">
    <h1 class="text-4xl text-left md:text-8xl font-heading">
      The <br /> Stack &amp; <br /> Tools
    </h1>
    <h1 class="text-4xl text-right md:text-8xl font-heading">
      Used to <br />
      <EncryptedText
        texts={["Design", "Develop", "Deploy"]}
        class="uppercase"
      /><br />the app
    </h1>
  </div>

  <ul
    class="mt-8 grid w-full list-none grid-cols-3 gap-2 p-0 sm:grid-cols-4 sm:gap-3 lg:grid-cols-8"
    aria-label="Periodic table of my skills"
  >
    {#each TECH_STACKS as skill, index (skill.name)}
      {@const isDimmed =
        activeGroups.size > 0 && !activeGroups.has(skill.group)}
      <li
        class="grid aspect-square min-w-0 grid-rows-[auto_1fr_auto] rounded-sm border p-2 transition-opacity duration-200 motion-reduce:transition-none sm:p-3 lg:nth-[2]:col-start-8 lg:nth-[5]:col-start-5 lg:nth-[17]:col-start-3 {skill.groupStyle}"
        class:opacity-20={isDimmed}
        aria-label={`${skill.name}, ${skill.group}`}
      >
        <div class="flex items-center justify-between gap-2" aria-hidden="true">
          <span class="text-[10px] leading-none tabular-nums sm:text-xs">
            {String(index + 1).padStart(2, "0")}
          </span>
          <img
            src={skill.icon}
            alt=""
            class="md:size-8 size-5 shrink-0 object-contain"
            loading="lazy"
          />
        </div>
        <span
          class="self-center text-center text-3xl font-medium tracking-tight sm:text-4xl xl:text-5xl"
          aria-hidden="true"
        >
          {skill.symbol}
        </span>
        <span
          class="text-center text-[10px] leading-tight text-balance sm:text-xs"
        >
          {skill.name}
        </span>
      </li>
    {/each}
  </ul>

  <div
    class={isLegendFloating ? "flow-root h-(--legend-height)" : "flow-root"}
    style:--legend-height={`${legendHeight}px`}
  >
    <ul
      use:measureLegend
      class={isLegendFloating
        ? "animate-in gap-2 fade-in slide-in-from-bottom-[calc(100%+2rem)] duration-300 ease-out motion-reduce:animate-none bottom-[calc(1rem+env(safe-area-inset-bottom,0px))] fixed inset-x-4 z-40 mx-auto flex w-fit max-w-[calc(100%-2rem)] list-none flex-row flex-nowrap justify-start overflow-x-auto scrollbar-none [&::-webkit-scrollbar]:hidden md:justify-center rounded-2xl p-2 shadow-lg bg-transparent"
        : "mt-8 flex w-full gap-2 list-none flex-row flex-nowrap justify-start overflow-x-auto scrollbar-none [&::-webkit-scrollbar]:hidden p-0 sm:mt-10 md:justify-center"}
      aria-label="Skill group legend"
    >
      {#each groups as group (group.name)}
        <li class="shrink-0 whitespace-nowrap text-xs text-zinc-300 sm:text-sm">
          <button
            type="button"
            class="flex items-center gap-2 rounded-lg border border-transparent px-4 py-2 bg-white/10 backdrop-blur-lg aria-pressed:border-zinc-500 aria-pressed:bg-white/10 aria-pressed:text-white"
            aria-pressed={selectedGroup === group.name}
            onpointerenter={(event) => {
              if (event.pointerType === "mouse") {
                hoveredGroup = group.name;
              }
            }}
            onpointerleave={() => {
              hoveredGroup = null;
            }}
            onclick={() => {
              selectedGroup = selectedGroup === group.name ? null : group.name;
              hoveredGroup = null;
            }}
          >
            <span
              class="size-3 shrink-0 rounded-xs border {group.style}"
              aria-hidden="true"
            ></span>
            {group.name}
          </button>
        </li>
      {/each}
    </ul>
  </div>
</section>
