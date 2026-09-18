<script lang="ts">
  import "./layout.css";
  import favicon from "$lib/assets/favicon.svg";
  import { onMount } from "svelte";
  import LocomotiveScroll from "locomotive-scroll";

  onMount(() => {
    const scroll = new LocomotiveScroll();

    return () => {
      scroll.destroy();
    };
  });
  let { children } = $props();
</script>

<svelte:head>
  <title>Adics</title>
  <meta name="description" content="Pre-AI Programmer" />
  <link rel="icon" href={favicon} />
</svelte:head>
{@render children()}
