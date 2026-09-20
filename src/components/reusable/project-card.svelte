<script lang="ts">
  import ArrowUpRightIcon from "phosphor-svelte/lib/ArrowUpRightIcon";
  import { replaceCursorState } from "@/$lib/shared-state.svelte";
  import type { Project } from "@/lib/constants/projects";
  import { cx } from "class-variance-authority";

  const { title, description, hashtag, imgUrl, demoUrl, customClass }: Project =
    $props();

  let isHovered = $state(false);
  let isPressed = $state(false);
  let cursorPosition = $state({ x: 0, y: 0 });

  function updateCursorPosition(event: PointerEvent) {
    cursorPosition = { x: event.clientX, y: event.clientY };
  }
</script>

<div
  class={cx(
    "flex justify-between items-center gap-8 cursor-none rounded-sm overflow-hidden",
    customClass.background,
  )}
  role="presentation"
  onpointerenter={(event) => {
    isHovered = true;
    replaceCursorState.value = true;
    updateCursorPosition(event);
  }}
  onpointerleave={() => {
    isHovered = false;
    isPressed = false;
    replaceCursorState.value = false;
  }}
  onpointerdown={() => (isPressed = true)}
  onpointerup={() => (isPressed = false)}
  onpointercancel={() => (isPressed = false)}
  onpointermove={updateCursorPosition}
  onclick={() => window.open(demoUrl, "_blank")}
>
  <div
    class={cx("w-1/2 flex flex-col gap-8 items-start p-8", customClass.title)}
  >
    <div>
      <h2 class="text-6xl font-heading">{title}</h2>
      <p class={cx("text-lg max-w-2/3 line-clamp-3", customClass.description)}>
        {description}
      </p>
    </div>
    <div class="flex items-center gap-2">
      {#each hashtag as tag}
        <p class="text-xs"><span class="font-bold">#</span>{tag}</p>
      {/each}
    </div>
  </div>
  <div class="aspect-video w-1/2 overflow-hidden">
    <img src={imgUrl} alt={title} />
  </div>
</div>

<div
  class={cx(
    "pointer-events-none fixed z-50 -translate-x-1/2 -translate-y-1/2 rounded-full p-4 transition-[opacity,transform] duration-200 ease-out",
    customClass.cursorBackground,
  )}
  class:opacity-0={!isHovered}
  class:scale-0={!isHovered}
  class:scale-75={isHovered && isPressed}
  style:left={`${cursorPosition.x}px`}
  style:top={`${cursorPosition.y}px`}
  aria-hidden="true"
>
  <ArrowUpRightIcon
    weight="regular"
    size={24}
    fill={customClass.cursorForeground}
  />
</div>
