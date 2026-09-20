<script lang="ts">
  import ScrollReveal from "@/$lib/components/svelte-bits/ScrollReveal.svelte";
</script>

<section class="h-[60vh] bg-black md:px-0 px-8 py-24">
  <div
    class="container mx-auto h-max text-white md:max-w-6xl"
    data-scroll
    data-scroll-speed="0.08"
  >
    <ScrollReveal
      text="I live in Jakarta, Indonesia. Graduated from vocational high school in
      2023 majoring in Software Engineering. Since then, I&apos;ve been learning
      by building and working with teams to solve practical business problems."
      textClassName="md:text-7xl text-8xl font-bold font-heading text-center"
      baseRotation={0}
      enableBlur={false}
      wordAnimationStart="top bottom-=20%"
      wordAnimationEnd="top 50%"
      scrub={true}
    />
  </div>
</section>
