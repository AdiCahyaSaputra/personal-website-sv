"""Render saved display materials and compare smooth regions against source screenshot colors."""
import math
from pathlib import Path
from statistics import mean
import tempfile

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

root = Path(__file__).resolve().parents[2]


def srgb(value):
    return 12.92 * value if value <= 0.0031308 else 1.055 * value ** (1 / 2.4) - 0.055


def pixel(*, pixels, width, x, y):
    start = (y * width + x) * 4
    return tuple(srgb(value) for value in pixels[start:start + 3])


with tempfile.TemporaryDirectory(prefix='macbook-preview-colors-') as temporary:
    for project in ('twillink', 'yufo', 'forumgw'):
        bpy.ops.wm.open_mainfile(filepath=str(root / 'design/project-scenes' / f'{project}.blend'))
        scene = bpy.context.scene
        display = bpy.data.objects['Screenshot display']
        nodes = display.active_material.node_tree.nodes
        source = next(node.image for node in nodes if node.type == 'TEX_IMAGE'
                      and node.image.colorspace_settings.name == 'sRGB')
        source_pixels = source.pixels[:]
        source_width, source_height = source.size
        corners = [display.matrix_world @ vertex.co for vertex in display.data.vertices]
        center = sum(corners, Vector()) / 4
        normal = display.matrix_world.to_quaternion() @ Vector((0, -1, 0))
        camera = scene.camera
        camera.location = center + normal * 6
        camera.rotation_euler = (-normal).to_track_quat('-Z', 'Y').to_euler()
        camera.data.type = 'ORTHO'
        camera.data.ortho_scale = 3.1
        scene.render.resolution_x = 1200
        scene.render.resolution_y = 800
        scene.render.resolution_percentage = 100
        scene.cycles.samples = 1
        scene.cycles.use_denoising = False
        scene.render.filepath = str(Path(temporary) / f'{project}.png')

        for obj in scene.objects:
            obj.hide_render = obj not in (display, camera)

        bpy.ops.render.render(write_still=True)
        rendered = bpy.data.images.load(scene.render.filepath, check_existing=False)
        rendered_pixels = rendered.pixels[:]
        width, height = rendered.size
        projected = [world_to_camera_view(scene, camera, corner) for corner in corners]
        left, bottom = projected[0].x * width, projected[0].y * height
        right, top = projected[2].x * width, projected[2].y * height
        uv = [loop.uv.copy() for loop in display.data.uv_layers.active.data]
        sample_radius = max(2, math.ceil(2 * max(
            source_width * (uv[2].x - uv[0].x) / (right - left),
            source_height * (uv[2].y - uv[0].y) / (top - bottom))))
        errors = []

        for row in range(1, 25):
            for column in range(1, 33):
                x = math.floor(left + (right - left) * column / 33)
                y = math.floor(bottom + (top - bottom) * row / 25)
                u = (x + 0.5 - left) / (right - left)
                v = (y + 0.5 - bottom) / (top - bottom)
                source_x = int((uv[0].x + u * (uv[2].x - uv[0].x)) * source_width)
                source_y = int((uv[0].y + v * (uv[2].y - uv[0].y)) * source_height)
                neighborhood = [pixel(pixels=source_pixels, width=source_width,
                                      x=source_x + dx, y=source_y + dy)
                                for dx in (-sample_radius, 0, sample_radius)
                                for dy in (-sample_radius, 0, sample_radius)]
                variation = max(max(color[channel] for color in neighborhood)
                                - min(color[channel] for color in neighborhood) for channel in range(3))

                if variation > 0.015:
                    continue

                expected = neighborhood[4]
                actual = pixel(pixels=rendered_pixels, width=width, x=x, y=y)
                errors.extend(abs(a - b) for a, b in zip(actual, expected))

        print(f'{project}: {len(errors) // 3} source samples, mean sRGB error {mean(errors):.4f}, max {max(errors):.4f}')
        assert len(errors) >= 150, f'{project}: too few smooth samples'
        assert mean(errors) < 0.01, f'{project}: mean color error {mean(errors):.4f}'
        assert max(errors) < 0.04, f'{project}: maximum color error {max(errors):.4f}'
