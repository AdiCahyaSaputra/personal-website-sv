export type Contact = {
  label: string;
  href: string | null;
  pendingLabel: string;
};

export const CONTACTS: Contact[] = [
  {
    label: "Email",
    href: "mailto:adics631@gmail.com",
    pendingLabel: "Address coming soon",
  },
  {
    label: "GitHub",
    href: "https://github.com/AdiCahyaSaputra",
    pendingLabel: "Profile coming soon",
  },
  {
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/adi-cs",
    pendingLabel: "Profile coming soon",
  },
];
