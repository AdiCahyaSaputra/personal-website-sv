<script lang="ts">
  import AnimatedMenu from "@/components/reusable/animated-menu.svelte";

  let scrollY = $state(0);
</script>

<svelte:window bind:scrollY />

<AnimatedMenu
  class={`fixed! ${scrollY > 0 ? "translate-y-4" : "translate-y-15"} left-1/2 -translate-1/2 z-999 transition-[width,translate]! mobile:top-[max(1.25rem,env(safe-area-inset-top))] mobile:translate-y-0 mobile:max-w-[calc(100%-2rem)]`}
  items={[
    { label: "Home", href: "#home" },
    { label: "Work", href: "#work" },
    { label: "Stack", href: "#stack" },
    { label: "Experience", href: "#experience" },
  ]}
/>
