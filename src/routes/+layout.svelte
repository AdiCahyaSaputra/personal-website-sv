<script lang="ts">
  import "./layout.css";
  let { children } = $props();
</script>

<svelte:head>
  <title>Adi Cahya Saputra — Full stack developer</title>
  <meta name="description" content="Adi Cahya Saputra, a full stack developer based in Jakarta, Indonesia. Selected web and mobile projects, preferred technologies, and experience." />
  <meta name="theme-color" content="#101010" />
  <link rel="icon" href="/favicon/favicon.ico" sizes="any" />
  <link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png" />
</svelte:head>

{@render children()}
