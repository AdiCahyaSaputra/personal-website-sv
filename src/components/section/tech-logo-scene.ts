import {
  AmbientLight, Box3, Color, DirectionalLight, ExtrudeGeometry, Group,
  Mesh, MeshStandardMaterial, OrthographicCamera, Scene, Vector3, WebGLRenderer,
} from "three";
import { SVGLoader } from "three/examples/jsm/loaders/SVGLoader.js";
import { techLogos } from "./tech-logos";

const sources = import.meta.glob<string>(
  "/static/assets/tech-stack/{svelte,typescript,python,laravel,go,pgsql,nextjs2,docker,redis,expo}.svg",
  { query: "?raw", import: "default", eager: true },
);

function createLogo(file: string) {
  const source = sources[`/static/assets/tech-stack/${file}.svg`];
  const document = new DOMParser().parseFromString(source, "image/svg+xml");

  // Remove the export background so the logo itself defines the silhouette.
  for (const path of document.querySelectorAll('path[fill="white"]')) {
    if (path.getAttribute("d") === "M0 0H32V32H0V0Z") path.remove();
  }

  // SVGLoader does not support gradient fills. Use their original first stop.
  for (const element of document.querySelectorAll('[fill^="url("]')) {
    const id = element.getAttribute("fill")?.match(/#([^)]*)/)?.[1];
    const stop = id ? document.getElementById(id)?.querySelector("stop") : null;
    element.setAttribute("fill", stop?.getAttribute("stop-color") ?? "#171717");
  }

  // These assets contain white marks intended for a dark background.
  if (file === "expo") {
    for (const element of document.querySelectorAll("path")) {
      element.setAttribute("fill", "#171717");
    }
  }

  if (file === "nextjs2") {
    document.querySelectorAll("path").forEach((path, index) => {
      path.setAttribute("fill", index === 0 ? "#171717" : "#ffffff");
    });
  }

  const svg = new SVGLoader().parse(new XMLSerializer().serializeToString(document));
  const artwork = new Group();
  const viewBox = document.documentElement.getAttribute("viewBox")?.split(/\s+/).map(Number);
  const depth = (viewBox?.[2] ?? 32) * 0.1;

  svg.paths.forEach((path, index) => {
    const color = new Color(path.color);
    const front = new MeshStandardMaterial({ color, roughness: 0.3, metalness: 0.15 });
    const edge = new MeshStandardMaterial({
      color: color.clone().multiplyScalar(0.55), roughness: 0.38, metalness: 0.2,
    });

    for (const shape of SVGLoader.createShapes(path)) {
      const geometry = new ExtrudeGeometry(shape, {
        depth, steps: 1, curveSegments: 16, bevelEnabled: true,
        bevelThickness: depth * 0.1, bevelSize: depth * 0.045, bevelSegments: 3,
      });
      const mesh = new Mesh(geometry, [front, edge]);
      mesh.position.z = index * depth * 0.025;
      artwork.add(mesh);
    }
  });

  const bounds = new Box3().setFromObject(artwork);
  const center = bounds.getCenter(new Vector3());
  const size = bounds.getSize(new Vector3());
  artwork.position.sub(center);

  const normalized = new Group();
  normalized.add(artwork);
  normalized.scale.set(1 / Math.max(size.x, size.y), -1 / Math.max(size.x, size.y), 1 / Math.max(size.x, size.y));

  const logo = new Group();
  logo.add(normalized);
  return logo;
}

export function createTechLogoScene(canvas: HTMLCanvasElement) {
  const renderer = new WebGLRenderer({ canvas, alpha: true, antialias: true });
  const scene = new Scene();
  const camera = new OrthographicCamera(-1, 1, 1, -1, 0.1, 2000);
  camera.position.z = 1000;

  scene.add(new AmbientLight(0xffffff, 2));
  const key = new DirectionalLight(0xffffff, 3);
  key.position.set(-300, 500, 800);
  scene.add(key);
  const rim = new DirectionalLight(0xddeaff, 2);
  rim.position.set(500, -100, 300);
  scene.add(rim);

  const logos = techLogos.map((technology) => {
    const logo = createLogo(technology.file);
    logo.rotation.set(technology.rx, technology.ry, technology.rz);
    scene.add(logo);
    return { logo, technology };
  });

  function resize() {
    const { width, height } = canvas.getBoundingClientRect();
    const mobile = width < 768;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(width, height, false);
    camera.left = -width / 2;
    camera.right = width / 2;
    camera.top = height / 2;
    camera.bottom = -height / 2;
    camera.updateProjectionMatrix();

    for (const { logo, technology } of logos) {
      logo.visible = !mobile || technology.mobileVisible;
      logo.scale.setScalar(technology.size * (mobile ? 0.5 : Math.min(width / 1280, 1.25)));
      const position = mobile ? technology.mobilePosition : technology.desktopPosition;
      logo.position.set((position.x / 100 - 0.5) * width, (0.5 - position.y / 100) * height, 0);
    }

    renderer.render(scene, camera);
  }

  const observer = new ResizeObserver(resize);
  observer.observe(canvas);
  resize();

  return () => {
    observer.disconnect();
    scene.traverse((object) => {
      if (object instanceof Mesh) {
        object.geometry.dispose();
        const materials = Array.isArray(object.material) ? object.material : [object.material];
        for (const material of materials) material.dispose();
      }
    });
    renderer.dispose();
  };
}
