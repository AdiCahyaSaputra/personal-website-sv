"""Check saved keyboard geometry; optionally render a top view with -- --preview PATH."""
import argparse
from itertools import combinations
from pathlib import Path
import sys

import bpy
from mathutils import Vector

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--preview', type=Path)
args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
directory = Path(__file__).resolve().parent


def bounds(obj):
    corners = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
    return tuple((min(point[axis] for point in corners), max(point[axis] for point in corners))
                 for axis in range(3))


for project in ('twillink', 'yufo', 'forumgw'):
    bpy.ops.wm.open_mainfile(filepath=str(directory / f'{project}.blend'))
    keys = [obj for obj in bpy.data.objects if obj.name.startswith('Key ')]
    assert len(keys) == 78, f'{project}: expected 78 keys, got {len(keys)}'
    recess = bounds(bpy.data.objects['Keyboard recess'])

    for key in keys:
        extent = bounds(key)

        for axis in (0, 1):
            assert recess[axis][0] < extent[axis][0] < extent[axis][1] < recess[axis][1], key.name

        assert abs(key.location.z - 0.89) < 0.000001, f'{key.name}: uneven height'

    for first, second in combinations(keys, 2):
        a, b = bounds(first), bounds(second)
        overlaps = all(min(a[axis][1], b[axis][1]) > max(a[axis][0], b[axis][0]) for axis in (0, 1))
        assert not overlaps, f'{project}: {first.name} overlaps {second.name}'

    for legend in (obj for obj in bpy.data.objects if obj.name.startswith('Legend ')):
        key = bpy.data.objects['Key ' + legend.name.removeprefix('Legend ')]
        extent, key_extent = bounds(legend), bounds(key)
        assert all(key_extent[axis][0] < extent[axis][0] < extent[axis][1] < key_extent[axis][1]
                   for axis in (0, 1)), f'{legend.name}: outside key'

    space = bpy.data.objects['Key Space bar']
    trackpad = bounds(bpy.data.objects['Glass trackpad'])
    assert trackpad[1][1] < bounds(space)[1][0], f'{project}: space bar overlaps trackpad'
    assert bpy.data.objects['Key Up Arrow'].location.y > bpy.data.objects['Key Down Arrow'].location.y
    print(f'{project}: 78 keys contained in recess, no overlaps, legends aligned, trackpad clear')

if args.preview:
    scene = bpy.context.scene
    camera = scene.camera
    camera.location = (0, 0.12, 6)
    camera.rotation_euler = (0, 0, 0)
    camera.data.type = 'ORTHO'
    camera.data.ortho_scale = 3.25
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.color_type = 'MATERIAL'
    scene.display.shading.show_shadows = True
    scene.display.shading.show_cavity = True
    scene.render.resolution_x = 1600
    scene.render.resolution_y = 800
    scene.render.resolution_percentage = 100
    scene.render.filepath = str(args.preview.resolve())

    for obj in scene.objects:
        is_display = obj.parent and obj.parent.name == 'Display hinge'

        if is_display:
            obj.hide_render = True

    bpy.ops.render.render(write_still=True)
