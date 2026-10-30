"""Check saved display insets; optionally render a front view with -- --preview PATH."""
import argparse
from pathlib import Path
import sys

import bpy
from mathutils import Vector

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--preview', type=Path)
args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
directory = Path(__file__).resolve().parent


def local_bounds(obj):
    corners = [obj.matrix_local @ Vector(corner) for corner in obj.bound_box]
    return tuple((min(point[axis] for point in corners), max(point[axis] for point in corners))
                 for axis in range(3))


def edge_insets(*, outer, inner):
    return (inner[0][0] - outer[0][0], outer[0][1] - inner[0][1],
            inner[2][0] - outer[2][0], outer[2][1] - inner[2][1])


for project in ('twillink', 'yufo', 'forumgw'):
    bpy.ops.wm.open_mainfile(filepath=str(directory / f'{project}.blend'))
    lid = bpy.data.objects['Display hinge']
    names = ('Aluminum display lid', 'Display glass', 'Screenshot display', 'Camera notch', 'FaceTime camera')
    objects = {name: bpy.data.objects[name] for name in names}
    assert all(obj.parent == lid for obj in objects.values()), f'{project}: inconsistent display parents'
    outer = local_bounds(objects['Aluminum display lid'])
    glass = local_bounds(objects['Display glass'])
    screen = local_bounds(objects['Screenshot display'])
    notch = local_bounds(objects['Camera notch'])

    for name, extent, expected in (('glass', glass, 0.025), ('screen', screen, 0.070)):
        insets = edge_insets(outer=outer, inner=extent)
        assert all(abs(inset - expected) < 0.000001 for inset in insets), f'{project}: {name} insets {insets}'

    assert screen[1][1] < glass[1][0], f'{project}: screenshot behind glass'
    assert abs(notch[0][0] + notch[0][1]) < 0.000001, f'{project}: notch off center'
    assert abs(notch[2][1] - glass[2][1]) < 0.000001, f'{project}: notch detached from top edge'
    assert notch[2][0] < screen[2][1] < notch[2][1], f'{project}: notch does not meet screen'
    print(f'{project}: equal screen insets 0.070, equal glass insets 0.025, notch aligned')

if args.preview:
    scene = bpy.context.scene
    camera = scene.camera
    camera.location = lid.matrix_world @ Vector((0, -6, 1.015))
    target = lid.matrix_world @ Vector((0, 0, 1.015))
    camera.rotation_euler = (target - camera.location).to_track_quat('-Z', 'Y').to_euler()
    camera.data.type = 'ORTHO'
    camera.data.ortho_scale = 3.35
    scene.render.engine = 'BLENDER_WORKBENCH'
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.color_type = 'MATERIAL'
    scene.display.shading.show_shadows = False
    scene.display.shading.show_cavity = True
    scene.render.resolution_x = 1400
    scene.render.resolution_y = 950
    scene.render.resolution_percentage = 100
    scene.render.filepath = str(args.preview.resolve())

    for obj in scene.objects:
        if obj != camera:
            obj.hide_render = obj.name not in names

    bpy.ops.render.render(write_still=True)
