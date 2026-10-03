<script lang="ts">
  import ArrowDownIcon from "phosphor-svelte/lib/ArrowDownIcon";
  import DownloadSimpleIcon from "phosphor-svelte/lib/DownloadSimpleIcon";
</script>

<section
  id="about"
  class="shell flex min-h-[min(900px,100svh)] flex-col justify-center pt-[150px] pb-16 mobile:min-h-auto mobile:pt-32 mobile:pb-12"
  aria-labelledby="name"
  tabindex="-1"
>
  <h1
    id="name"
    class="font-heading text-[clamp(6rem,15.8vw,14rem)] leading-[0.84] font-normal tracking-[-0.025em] min-[1500px]:text-[15rem] mobile:text-[clamp(5.8rem,21vw,10rem)]"
  >
    <span class="block overflow-hidden pt-[0.06em] [&>span]:inline-block"
      ><span data-intro>Adi Cahya</span></span
    >
    <span class="block overflow-hidden pt-[0.06em] [&>span]:inline-block"
      ><span data-intro>Saputra<span class="text-red-600">.</span></span></span
    >
  </h1>
  <div
    class="mt-12 flex mobile:mt-8 mobile:grid-cols-[1fr] mobile:gap-9 w-full"
    data-intro
  >
    <div class="max-w-[420px] mobile:row-start-1">
      <p class="text-[15px] leading-[1.8] text-muted mobile:text-[14px]">
        Pre-AI Programmer. I build full stack web <br
          class="mobile:hidden"
        />and mobile apps for at least 3 years.
      </p>

      <a
        class="text-link mt-5"
        href="/assets/doc/resume-adi-cahya-saputra.pdf"
        download="Adi-Cahya-Saputra-CV.pdf"
      >
        Download My CV <DownloadSimpleIcon size={17} />
      </a>
    </div>
  </div>
</section>
