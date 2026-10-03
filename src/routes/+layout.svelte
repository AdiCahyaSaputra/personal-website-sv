<script lang="ts">
  import "./layout.css";
  let { children } = $props();
</script>

<svelte:head>
  <title>Adi Cahya Saputra — Full-Stack Developer</title>
  <meta
    name="description"
    content="Portfolio of Adi Cahya Saputra, a full-stack developer in Jakarta building web and mobile products."
  />
  <meta name="theme-color" content="#101010" />
  <link rel="icon" href="/favicon/favicon.ico" />
  <link rel="icon" href="/favicon/favicon-16x16.png" sizes="16x16" type="image/png" />
  <link rel="icon" href="/favicon/favicon-32x32.png" sizes="32x32" type="image/png" />
  <link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png" />
  <link rel="manifest" href="/favicon/site.webmanifest" />

  <meta property="og:title" content="Adi Cahya Saputra — Full-Stack Developer" />
  <meta
    property="og:description"
    content="Selected web and mobile product work by Adi Cahya Saputra."
  />
  <meta property="og:url" content="https://adics.xyz" />
  <meta property="og:site_name" content="Adi Cahya Saputra" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="https://adics.xyz/og.png" />
</svelte:head>

{@render children()}
