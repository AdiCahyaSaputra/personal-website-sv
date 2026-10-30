# Project studio scenes

Original procedural Blender scenes for the home page project section. A graphite laptop modeled with 14-inch MacBook Pro proportions sits on a charcoal stone plinth, against a paneled plaster wall. Twillink uses violet lighting, Yufo amber, and ForumGW green. The hardware is an approximate visualization, not an exact Apple CAD model.

Each `.blend` includes its screenshot texture, camera, lights, and materials. Open it in Blender and render with F12. The original screenshots remain unchanged in `static/assets/project/`; ForumGW's presentation board is cropped through the display UVs.

Regenerate all scenes with Blender 5.2:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --background --python design/project-scenes/render.py
uv run design/project-scenes/export.py
```

Append `-- --project twillink --draft` to the Blender command for a fast preview. Draft mode overwrites that project's PNG and Blender file; rerun without `--draft` before exporting the website assets.

Final renders are 1400 × 1050 PNGs under `static/assets/project-scenes/`. The exporter creates compressed WebP copies used by the project section. To change the palette, edit `PROJECTS` in `render.py`. To replace a screenshot, update the corresponding original WebP and regenerate.

The approved layout exploration is archived on the local Git branch `prototype/projects-approved`. The selected stacked cards are implemented in `src/components/section/project-section.svelte`.
