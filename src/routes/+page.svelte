<script lang="ts">
  import { dev } from "$app/environment";
  import { page } from "$app/state";
  import BottomBlur from "@/components/reusable/bottom-blur.svelte";
  import Navbar from "@/components/reusable/navbar.svelte";

  import HallSection from "@/components/section/hall-section.svelte";
  import ProjectSection from "@/components/section/project-section.svelte";
  import SkillSection from "@/components/section/skill-section.svelte";
  import ExperienceSection from "@/components/section/experience-section.svelte";
</script>

<main class="relative overflow-x-hidden bg-foreground">
  <Navbar />
  <BottomBlur />

  <HallSection />
  <ProjectSection />
  <SkillSection />
  <ExperienceSection />
</main>
