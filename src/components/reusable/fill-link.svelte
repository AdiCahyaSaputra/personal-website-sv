<script lang="ts">
  import type { Snippet } from "svelte";
  import type { HTMLAnchorAttributes } from "svelte/elements";

  let {
    children,
    class: className,
    ...attributes
  }: HTMLAnchorAttributes & { href: string; children: Snippet } = $props();
</script>

<a
  {...attributes}
  class={[
    "relative isolate px-4 inline-flex min-h-11 items-center gap-2 overflow-hidden border border-[#737373] text-[13px] transition-[color,border-color] duration-300 ease-out",
    "before:pointer-events-none before:absolute before:inset-0 before:-z-10 before:translate-y-full before:bg-[#f5f5f5] before:transition-transform before:duration-300 before:ease-out",
    "hover:border-[#f5f5f5] hover:text-[#101010] hover:before:translate-y-0 focus-visible:border-[#f5f5f5] focus-visible:text-[#101010] focus-visible:before:translate-y-0",
    "motion-reduce:transition-none motion-reduce:before:transition-none",
    className,
  ]}
>
  {@render children()}
</a>
