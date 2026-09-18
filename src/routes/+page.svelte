<script lang="ts">
  import HallSection from "@/components/section/hall-section.svelte";
  import ProfileSection from "@/components/section/profile-section.svelte";
  import TargetCursor from "@/$lib/components/svelte-bits/TargetCursor.svelte";
</script>

<main
  class="selection:text-black selection:bg-white bg-black"
  data-scroll-container
>
  <TargetCursor hideDefaultCursor />

  <HallSection />
  <ProfileSection />
</main>
