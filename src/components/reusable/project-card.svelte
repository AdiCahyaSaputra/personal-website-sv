<script lang="ts">
  import ArrowUpRightIcon from "phosphor-svelte/lib/ArrowUpRightIcon";
  import { replaceCursorState } from "@/$lib/shared-state.svelte";

  const { title, description, relatedPlace, imgUrl } = $props();

  let isHovered = $state(false);
  let isPressed = $state(false);
  let cursorPosition = $state({ x: 0, y: 0 });

  function updateCursorPosition(event: PointerEvent) {
    cursorPosition = { x: event.clientX, y: event.clientY };
  }
</script>

<div
  class="flex justify-between items-center gap-8 cursor-none"
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
>
  <div class="text-white w-1/2 flex flex-col gap-2 items-start">
    <div>
      <h2 class="text-6xl font-heading">{title}</h2>
      <p class="text-white/60 text-lg max-w-2/3">{description}</p>
    </div>
    <div class="flex items-end gap-2">
      <div class="size-4 relative">
        <div
          class="absolute border-l border-b border-white/60 w-4 h-2 left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2"
        ></div>
      </div>
      <p class="text-sm leading-3">developed when i'm at {relatedPlace}</p>
    </div>
  </div>
  <div class="aspect-video w-1/2">
    <img src={imgUrl} alt={title} />
  </div>
</div>

<div
  class="pointer-events-none fixed z-50 -translate-x-1/2 -translate-y-1/2 border border-black rounded-full bg-white p-8 transition-[opacity,transform] duration-200 ease-out"
  class:opacity-0={!isHovered}
  class:scale-0={!isHovered}
  class:scale-75={isHovered && isPressed}
  style:left={`${cursorPosition.x}px`}
  style:top={`${cursorPosition.y}px`}
  aria-hidden="true"
>
  <ArrowUpRightIcon weight="fill" size={32} fill="black" />
</div>
