<script lang="ts">
  import { cx } from "class-variance-authority";

  let { icon, name, iconClass = "", wrapperClass = "" } = $props();
</script>

<li
  class={cx(
    "cursor-target relative grid aspect-square w-[clamp(3rem,8vw,4.25rem)] place-items-center rounded-none max-[30rem]:w-11",
    wrapperClass,
  )}
>
  <span class="group relative grid h-full w-full place-items-center">
    <img
      class={cx(
        "size-[clamp(1.5rem,4vw,2rem)] object-contain grayscale group-hover:grayscale-0",
        iconClass,
      )}
      src={icon}
      alt={name}
    />
    <span
      class="pointer-events-none absolute bottom-[calc(100%+1rem)] left-1/2 z-10 w-max max-w-[min(14rem,calc(100vw-2rem))] translate-x-[-50%] translate-y-1 rounded-none bg-red-600 px-2 py-1 text-center text-xs leading-tight text-white opacity-0 transition-[opacity,transform] duration-150 ease-in group-hover:translate-y-0 group-hover:opacity-100 group-focus-within:translate-y-0 group-focus-within:opacity-100"
      role="tooltip">{name}</span
    >
  </span>
</li>
