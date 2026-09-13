<script lang="ts">
  import "./layout.css";
  import favicon from "$lib/assets/favicon.svg";

  let { children } = $props();
</script>

<svelte:head>
  <title>Adics</title>
  <meta name="description" content="Pre-AI Programmer" />
  <link rel="icon" href={favicon} />
</svelte:head>
{@render children()}
