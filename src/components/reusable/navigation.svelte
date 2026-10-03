<script lang="ts">
  import { gsap } from "gsap";
  import ArrowUpRightIcon from "phosphor-svelte/lib/ArrowUpRightIcon";
  import ContactLinks from "./contact-links.svelte";
  import MinecraftHead from "./minecraft-head.svelte";

  const links = [
    { href: "#about", label: "About" },
    { href: "#projects", label: "Selected work" },
    { href: "#stack", label: "Tech stack" },
    { href: "#experience", label: "Experience" },
    { href: "#contact", label: "Contact" },
  ];

  let dialog: HTMLDialogElement;
  let menuOpen = $state(false);
  let timeline: gsap.core.Timeline | undefined;
  let previousOverflow = "";
  let closing = false;

  function openMenu() {
    if (dialog.open) return;
    previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    dialog.showModal();
    menuOpen = true;
    closing = false;
    const reducedMotion = window.matchMedia(
      "(prefers-reduced-motion: reduce)",
    ).matches;
    timeline?.kill();
    timeline = gsap
      .timeline()
      .fromTo(
        dialog.querySelectorAll("[data-menu-line]"),
        { y: (index) => index === 0 ? -3.5 : 3.5, rotation: 0 },
        {
          y: 0,
          rotation: (index) => index === 0 ? 45 : -45,
          duration: reducedMotion ? 0 : 0.35,
          ease: "power3.inOut",
        },
        0,
      )
      .fromTo(
        dialog,
        { clipPath: "inset(0 0 100% 0)" },
        {
          clipPath: "inset(0 0 0% 0)",
          duration: reducedMotion ? 0 : 0.55,
          ease: "power3.inOut",
        },
        0,
      )
      .fromTo(
        dialog.querySelectorAll(".menu-link"),
        { y: reducedMotion ? 0 : 35, opacity: 0 },
        {
          y: 0,
          opacity: 1,
          duration: reducedMotion ? 0 : 0.4,
          stagger: reducedMotion ? 0 : 0.045,
          ease: "power3.out",
        },
        reducedMotion ? 0 : 0.2,
      );
  }

  function restoreScroll() {
    document.body.style.overflow = previousOverflow;
    menuOpen = false;
    closing = false;
  }

  function closeMenu(destination?: string) {
    if (closing || !dialog.open) return;
    closing = true;
    timeline?.kill();
    const finish = () => {
      dialog.close();
      restoreScroll();
      if (destination) {
        window.location.hash = destination;
        document
          .querySelector<HTMLElement>(destination)
          ?.focus({ preventScroll: true });
      }
    };
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      finish();
      return;
    }
    timeline = gsap.timeline({ onComplete: finish })
      .to(dialog.querySelectorAll("[data-menu-line]"), {
        y: (index) => index === 0 ? -3.5 : 3.5,
        rotation: 0,
        duration: 0.25,
        ease: "power3.inOut",
      }, 0)
      .to(dialog, {
        clipPath: "inset(0 0 100% 0)",
        duration: 0.35,
        ease: "power3.inOut",
      }, 0);
  }

  function navigate(event: MouseEvent, destination: string) {
    if (
      event.metaKey ||
      event.ctrlKey ||
      event.shiftKey ||
      event.altKey ||
      event.button !== 0
    )
      return;
    event.preventDefault();
    closeMenu(destination);
  }

  function trapFocus(event: KeyboardEvent) {
    if (event.key !== "Tab") return;
    const controls = dialog.querySelectorAll<HTMLElement>(
      "a[href], button:not([disabled])",
    );
    const first = controls.item(0);
    const last = controls.item(controls.length - 1);
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last?.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first?.focus();
    }
  }

  function initializeDialog(element: HTMLDialogElement) {
    dialog = element;
    return () => {
      timeline?.kill();
      if (element.open) document.body.style.overflow = previousOverflow;
    };
  }
</script>

{#snippet menuIcon()}
  <span class="relative block size-6" aria-hidden="true">
    <span
      class="absolute top-1/2 left-0 -mt-[0.5px] h-px w-6 origin-center bg-current"
      style="transform: translateY(-3.5px)"
      data-menu-line
    ></span>
    <span
      class="absolute top-1/2 left-0 -mt-[0.5px] h-px w-6 origin-center bg-current"
      style="transform: translateY(3.5px)"
      data-menu-line
    ></span>
  </span>
{/snippet}

<header class="fixed inset-x-0 top-0 z-30 bg-[#101010]/30 backdrop-blur-md">
  <div class="shell flex h-23 items-center justify-between mobile:h-19">
    <a
      class="block size-11"
      href="#about"
      aria-label="Adi Cahya Saputra, back to top"
    >
      <MinecraftHead />
    </a>
    <button
      class="flex min-h-11 items-center [justify-content:end] gap-4.5 py-3 pr-0 pl-4 text-[12px] hover:text-white/40"
      onclick={openMenu}
      aria-label="Open menu"
      aria-haspopup="dialog"
      aria-expanded={menuOpen}
      aria-controls="site-menu"
    >
      {@render menuIcon()}
    </button>
  </div>
</header>

<dialog
  class="fixed inset-0 m-0 h-dvh max-h-none w-full max-w-none overflow-y-auto border-0 bg-surface p-0 text-[#f5f5f5] backdrop:bg-transparent"
  {@attach initializeDialog}
  id="site-menu"
  aria-label="Site navigation"
  onkeydown={trapFocus}
  oncancel={(event) => {
    event.preventDefault();
    closeMenu();
  }}
  onclose={restoreScroll}
>
  <div class="shell flex min-h-full flex-col">
    <div class="flex h-23 shrink-0 items-center justify-between mobile:h-19">
      <a
        class="block size-11"
        href="#about"
        onclick={(event) => navigate(event, "#about")}
        aria-label="Adi Cahya Saputra, back to top"
      >
        <MinecraftHead />
      </a>
      <button
        class="flex min-h-11 items-center [justify-content:end] gap-4.5 py-3 pr-0 pl-4 text-[12px] hover:text-white/40"
        onclick={() => closeMenu()}
        aria-label="Close menu"
        >{@render menuIcon()}</button
      >
    </div>
    <div
      class="grid flex-1 grid-cols-[1fr_2fr] [align-items:start] py-10 mobile:grid-cols-[1fr] mobile:content-center mobile:gap-7 mobile:pt-6 mobile:pb-10"
    >
      <p class="eyebrow mt-4 text-muted mobile:m-0">Take a look around</p>
      <nav class="flex flex-col" aria-label="Main navigation">
        {#each links as link (link.href)}
          <a
            class="menu-link group flex items-center justify-between gap-5 font-heading text-[clamp(42px,6.7vw,92px)] leading-[1.15] transition-[color] duration-200 ease-[ease] hover:text-accent mobile:text-[clamp(42px,10.5vw,72px)] mobile:leading-[1.25]"
            href={link.href}
            onclick={(event) => navigate(event, link.href)}
            ><span>{link.label}</span><ArrowUpRightIcon
              size={36}
              class="opacity-0 transition-opacity duration-200 ease-[ease] group-hover:opacity-100 group-focus-visible:opacity-100 mobile:w-6 mobile:text-muted mobile:opacity-100"
            /></a
          >
        {/each}
      </nav>
    </div>
    <div
      class="flex items-center justify-between gap-6 border-t border-t-line py-6 text-[12px] leading-[1.8] mobile:flex-col mobile:[align-items:start] mobile:gap-3"
    >
      <p>
        Adi Cahya Saputra<br /><span class="text-[11px] text-muted"
          >Full stack developer · Jakarta, ID</span
        >
      </p>
      <ContactLinks compact />
    </div>
  </div>
</dialog>
