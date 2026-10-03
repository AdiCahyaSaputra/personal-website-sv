<script lang="ts">
  import { animatePortfolio } from "$lib/animations/portfolio";
  import Navigation from "@/components/reusable/navigation.svelte";
  import HallSection from "@/components/section/hall-section.svelte";
  import ProfileSection from "@/components/section/profile-section.svelte";
  import ProjectSection from "@/components/section/project-section.svelte";
  import TechStackSection from "@/components/section/tech-stack-section.svelte";
  import ExperienceSection from "@/components/section/experience-section.svelte";
  import ContactSection from "@/components/section/contact-section.svelte";

</script>

<a
  class="fixed top-3 left-5 z-40 -translate-y-[200%] bg-white px-5 py-3 text-black focus:translate-y-0"
  href="#main">Skip to content</a
>
<Navigation />
<main id="main" tabindex="-1" {@attach animatePortfolio}>
  <HallSection />
  <ProfileSection />
  <ProjectSection />
  <TechStackSection />
  <ExperienceSection />
  <ContactSection />
</main>
