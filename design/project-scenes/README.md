# Project studio scenes

Original procedural Blender scenes for the home page project section. A graphite laptop modeled with 14-inch MacBook Pro proportions sits on a charcoal stone plinth, against a paneled plaster wall. Twillink uses violet lighting, Yufo amber, and ForumGW green. The hardware is an approximate visualization, not an exact Apple CAD model.

Each `.blend` includes its screenshot texture, camera, lights, and materials. Open it in Blender and render with F12. The original screenshots remain unchanged in `static/assets/project/`; ForumGW's presentation board is cropped through the display UVs.

Regenerate all scenes with Blender 5.2:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --background --python design/project-scenes/render.py
uv run design/project-scenes/export.py
```

Append `-- --project twillink --draft` to the Blender command for a fast preview. Draft mode overwrites that project's PNG and Blender file; rerun without `--draft` before exporting the website assets.

The keyboard uses a staggered 78-key ANSI layout, with a short function row, wider modifiers, and inverted-T arrow keys. Check all saved scenes for overlapping keys, misplaced legends, and recess containment with:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --background --python design/project-scenes/verify-keyboard.py
```

Append `-- --preview /tmp/macbook-keyboard.png` to also render a top view without changing the saved scenes.

The display opening and cover glass each use a uniform inset from the lid on all four edges. Verify the saved geometry and optionally render a straight-on view with:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --background --python design/project-scenes/verify-display.py -- --preview /tmp/macbook-display.png
```

Camera-visible screenshot textures use Blender's `AgX Base sRGB` inverse view transform and an unlit emission surface to preserve the source colors through AgX. Other rays keep the original screen material so the surrounding lighting and reflections retain their appearance. Render the saved display materials and compare their colors with the source screenshots using:

```sh
/Applications/Blender.app/Contents/MacOS/Blender --background --python-exit-code 1 --python design/project-scenes/verify-preview-colors.py
```

Final renders are 2800 × 2100 PNGs under `static/assets/project-scenes/`. The exporter creates quality-95 WebP copies used by the project section. To change the palette, edit `PROJECTS` in `render.py`. To replace a screenshot, update the corresponding original WebP and regenerate.

The approved layout exploration is archived on the local Git branch `prototype/projects-approved`. The selected stacked cards are implemented in `src/components/section/project-section.svelte`.
