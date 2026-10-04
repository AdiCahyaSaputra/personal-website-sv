<script lang="ts">
  import ArrowUpIcon from "phosphor-svelte/lib/ArrowUpIcon";
  import ContactLinks from "../reusable/contact-links.svelte";
</script>

<section
  id="contact"
  class="section shell pb-16 mobile:pb-16"
  aria-labelledby="contact-heading"
  tabindex="-1"
>
  <div>
    <h2
      id="contact-heading"
      class="mt-8 font-heading text-[clamp(6rem,16vw,15rem)] leading-none tracking-tight"
    >
      Let’s talk<span class="text-red-600">.</span>
    </h2>
    <p class="mt-5 mb-12 max-w-82.5 text-[14px] leading-[1.8] text-muted">
      For a project, a collaboration, or a conversation about building software.
    </p>
    <ContactLinks />
  </div>
</section>
<footer
  class="shell flex items-center justify-between gap-6 border-t border-t-line py-7 text-[11px] text-muted mobile:flex-col mobile:[align-items:start] mobile:gap-3"
>
  <p>© {new Date().getFullYear()} Adi Cahya Saputra</p>
  <a href="#hall" class="flex min-h-11 items-center gap-4 hover:text-white">
    Back to top <ArrowUpIcon size={16} />
  </a>
</footer>
