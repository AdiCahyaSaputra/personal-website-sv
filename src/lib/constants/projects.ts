type CustomProjectCardClass = {
  title: string;
  description: string;
  relatedPlaceArrow: string;
  background: string;
  cursorBackground: string;
  cursorForeground: string;
};

export type Project = {
  title: string;
  description: string;
  hashtag: string[];
  imgUrl: string;
  customClass: CustomProjectCardClass;
  demoUrl?: string;
};

export const PROJECTS: Project[] = [
  {
    title: "twillink",
    description:
      "a ugc storefront where brands and creators collaborate and turn social content into a shoppable experience.",
    hashtag: ["crosva", "fullstack", "web"],
    imgUrl: "/assets/project/twillink.png",
    demoUrl: "https://twillink.com",
    customClass: {
      title: "text-gray-900",
      description: "text-gray-900/60",
      relatedPlaceArrow: "border-gray-900/30",
      background: "bg-white",
      cursorBackground: "bg-gray-900/30 backdrop-blur-md",
      cursorForeground: "white",
    },
  },
  {
    title: "yufo trade",
    description:
      "a supply platform for tradies, connecting product ordering, delivery, and supplier workflows across web and mobile.",
    hashtag: ["crosva", "fullstack", "web", "mobile"],
    imgUrl: "/assets/project/yufo.png",
    demoUrl: "https://yufotrade.com",
    customClass: {
      title: "text-white",
      description: "text-white/60",
      relatedPlaceArrow: "border-white/30",
      background: "bg-gray-900",
      cursorBackground: "bg-gray-600/30 backdrop-blur-md",
      cursorForeground: "white",
    },
  },
];
