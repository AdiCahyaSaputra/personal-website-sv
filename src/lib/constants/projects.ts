export type Project = {
  title: string;
  description: string;
  hashtag: string[];
  imgUrl: string;
  demoUrl?: string;
};

export const PROJECTS: Project[] = [
  {
    title: "twillink",
    description:
      "A UGC storefront where brands and creators collaborate and turn social content into a shoppable experience.",
    hashtag: ["crosva", "fullstack", "web"],
    imgUrl: "/assets/project/twillink.webp",
    demoUrl: "https://twillink.com",
  },
  {
    title: "yufo trade",
    description:
      "A supply platform for tradies, connecting product ordering, delivery, and supplier workflows across web and mobile.",
    hashtag: ["crosva", "fullstack", "web", "mobile"],
    imgUrl: "/assets/project/yufo.webp",
    demoUrl: "https://yufotrade.com",
  },
  {
    title: "forumgw",
    description:
      "A community forum for open and anonymous discussions, built with a type-safe web stack.",
    hashtag: ["personal", "fullstack", "web"],
    imgUrl: "/assets/project/forumgw.webp",
    demoUrl: "https://forumgw.vercel.app",
  },
];
