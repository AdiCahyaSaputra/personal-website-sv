export type Experience = {
  experience: string;
  year: number;
  type: "full-time" | "part-time";
  at: string;
  sameYear?: boolean;
};

export const EXPERIENCE: Experience[] = [
  {
    experience: "IT Support",
    year: 2023,
    type: "full-time",
    at: "at My Previous Vocational High School",
  },
  {
    experience: "Full Stack Web Developer",
    year: 2023,
    type: "part-time",
    at: "at Mitrain ID",
  },
  {
    experience: "Junior Software Engineer",
    year: 2024,
    type: "full-time",
    at: "at PT Pertamina Bina Medika IHC",
  },
  {
    experience: "Full Stack Developer",
    year: 2024,
    type: "full-time",
    at: "at PT Enakans Media Teknologi",
  },
  {
    experience: "Full Stack Developer",
    year: 2025,
    type: "part-time",
    at: "at Crosva",
  },
  {
    experience: "Python Backend Developer",
    year: 2026,
    type: "full-time",
    at: "at PT Claverio Transformasi Digital",
  },
];
