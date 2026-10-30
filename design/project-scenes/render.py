"""Run: Blender --background --python design/project-scenes/render.py
Pass -- --project twillink to render one scene, or -- --draft for a quick preview.
"""
import argparse
import math
from pathlib import Path
import sys

import bpy
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--project', choices=['twillink', 'yufo', 'forumgw'])
parser.add_argument('--draft', action='store_true')
args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
bpy.context.preferences.filepaths.save_version = 0

PROJECTS = {
    'twillink': ((0.075, 0.035, 0.28), (0.42, 0.25, 1.0)),
    'yufo': ((0.30, 0.075, 0.014), (1.0, 0.40, 0.10)),
    'forumgw': ((0.018, 0.14, 0.11), (0.15, 0.85, 0.60)),
}


def material(name, color, *, metallic=0, roughness=0.45):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1)
    mat.use_nodes = True
    shader = mat.node_tree.nodes.get('Principled BSDF')
    shader.inputs['Base Color'].default_value = (*color, 1)
    shader.inputs['Metallic'].default_value = metallic
    shader.inputs['Roughness'].default_value = roughness
    return mat


def box(name, *, location, size, mat, bevel=0.025, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)

    if bevel:
        modifier = obj.modifiers.new('Machined edges', 'BEVEL')
        modifier.width = bevel
        modifier.segments = 5
        obj.modifiers.new('Weighted normals', 'WEIGHTED_NORMAL')

    if parent:
        obj.parent = parent

    return obj


def area(name, *, location, target, color, energy, size):
    bpy.ops.object.light_add(type='AREA', location=location)
    light = bpy.context.object
    light.name = name
    light.data.energy = energy
    light.data.color = color
    light.data.shape = 'DISK'
    light.data.size = size
    light.rotation_euler = (Vector(target) - light.location).to_track_quat('-Z', 'Y').to_euler()
    return light


def keyboard(*, keys, marks):
    rows = [
        [('Escape', 1.5)] + [(f'F{index}', 1) for index in range(1, 13)] + [('Touch ID', 1.5)],
        [(key, 1) for key in '`1234567890-='] + [('Delete', 2)],
        [('Tab', 1.5)] + [(key, 1) for key in 'QWERTYUIOP[]'] + [('Backslash', 1.5)],
        [('Caps Lock', 1.75)] + [(key, 1) for key in "ASDFGHJKL;'"] + [('Return', 2.25)],
        [('Left Shift', 2.25)] + [(key, 1) for key in 'ZXCVBNM,./'] + [('Right Shift', 2.75)],
        [('Fn', 1), ('Control', 1), ('Left Option', 1), ('Left Command', 1.25),
         ('Space bar', 5.75), ('Right Command', 1.25), ('Right Option', 1),
         ('Left Arrow', 11 / 12), ('Down Arrow', 11 / 12), ('Right Arrow', 11 / 12)],
    ]
    pitch = 0.162
    gap = 0.018
    left = -15 * pitch / 2

    for row_index, row in enumerate(rows):
        x = left
        y = 0.57 - row_index * 0.164
        height = 0.095 if row_index == 0 else 0.14

        for name, units in row:
            width = units * pitch - gap
            center_x = x + units * pitch / 2
            is_arrow = name.endswith('Arrow')
            key_height = (height - gap) / 2 if is_arrow else height
            center_y = y - (height + gap) / 4 if is_arrow else y
            box(f'Key {name}', location=(center_x, center_y, 0.89),
                size=(width, key_height, 0.022), mat=keys, bevel=0.015)

            if name != 'Space bar':
                box(f'Legend {name}', location=(center_x, center_y, 0.902),
                    size=(0.033, 0.008, 0.001), mat=marks, bevel=0.002)

            if name == 'Down Arrow':
                up_y = y + (height + gap) / 4
                box('Key Up Arrow', location=(center_x, up_y, 0.89),
                    size=(width, key_height, 0.022), mat=keys, bevel=0.015)
                box('Legend Up Arrow', location=(center_x, up_y, 0.902),
                    size=(0.033, 0.008, 0.001), mat=marks, bevel=0.002)

            x += units * pitch


def scene(project, colors):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    wall_color, light_color = colors
    graphite = material('Space black anodized aluminum', (0.075, 0.080, 0.09), metallic=0.85, roughness=0.28)
    glass = material('Black display bezel', (0.006, 0.008, 0.012), roughness=0.23)
    keys = material('Keyboard polymer', (0.009, 0.010, 0.013), roughness=0.52)
    marks = material('Quiet key legends', (0.42, 0.43, 0.45), roughness=0.55)
    stone = material('Charcoal satin stone', (0.018, 0.023, 0.029), roughness=0.56)
    wall = material('Pigmented plaster', wall_color, roughness=0.73)
    nodes = wall.node_tree.nodes
    noise = nodes.new('ShaderNodeTexNoise')
    noise.inputs['Scale'].default_value = 95
    bump = nodes.new('ShaderNodeBump')
    bump.inputs['Strength'].default_value = 0.16
    bump.inputs['Distance'].default_value = 0.018
    wall.node_tree.links.new(noise.outputs['Fac'], bump.inputs['Height'])
    wall.node_tree.links.new(bump.outputs['Normal'], nodes.get('Principled BSDF').inputs['Normal'])

    box('Studio floor', location=(0, 0, -0.05), size=(200, 200, 0.1), mat=stone)
    box('Color backdrop', location=(0, 2.1, 3.1), size=(20, 0.25, 7), mat=wall, bevel=0.06)
    # Broad vertical fins make a quiet architectural background rather than a tiled wall.
    for index in range(-4, 5):
        box(f'Plaster fin {index}', location=(index * 1.85, 1.96, 3.1), size=(1.80, 0.16, 7), mat=wall, bevel=0.025)

    box('Floating slab plinth', location=(0, -0.10, 0.35), size=(4.8, 3.3, 0.70), mat=stone, bevel=0.17)
    box('Plinth recessed foot', location=(0, 0, 0.12), size=(3.6, 2.5, 0.24), mat=glass, bevel=0.08)

    # Hardware proportions follow the 14-inch chassis: 31.26 by 22.12 cm.
    box('MacBook lower chassis', location=(0, -0.20, 0.79), size=(3.126, 2.212, 0.155), mat=graphite, bevel=0.075)
    box('Keyboard recess', location=(0, 0.12, 0.875), size=(2.57, 1.04, 0.018), mat=glass, bevel=0.05)
    keyboard(keys=keys, marks=marks)
    box('Trackpad seam', location=(0, -0.83, 0.873), size=(1.25, 0.69, 0.008), mat=glass, bevel=0.055)
    box('Glass trackpad', location=(0, -0.83, 0.879), size=(1.23, 0.67, 0.008), mat=graphite, bevel=0.05)
    for side in [-1, 1]:
        for row in range(22):
            for col in range(3):
                box('Speaker perforation', location=(side * (1.36 + col * 0.033), 0.59 - row * 0.045, 0.872), size=(0.012, 0.022, 0.002), mat=glass, bevel=0.003)

    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0.81, 0.85))
    lid = bpy.context.object
    lid.name = 'Display hinge'
    lid.rotation_euler.x = math.radians(-7)
    lid_width, lid_height = 3.105, 2.03
    glass_inset = 0.025
    screen_inset = 0.070
    box('Aluminum display lid', location=(0, 0, lid_height / 2),
        size=(lid_width, 0.065, lid_height), mat=graphite, bevel=0.065, parent=lid)
    box('Display glass', location=(0, -0.038, lid_height / 2),
        size=(lid_width - 2 * glass_inset, 0.018, lid_height - 2 * glass_inset),
        mat=glass, bevel=0.055, parent=lid)

    screen = bpy.data.materials.new('Project screenshot')
    screen.use_nodes = True
    shader = screen.node_tree.nodes.get('Principled BSDF')
    image = bpy.data.images.load(str(ROOT / 'static/assets/project' / f'{project}.webp'), check_existing=True)
    image.pack()
    texture = screen.node_tree.nodes.new('ShaderNodeTexImage')
    texture.image = image
    screen.node_tree.links.new(texture.outputs['Color'], shader.inputs['Emission Color'])
    shader.inputs['Emission Strength'].default_value = 1.0
    shader.inputs['Base Color'].default_value = (0, 0, 0, 1)
    shader.inputs['Roughness'].default_value = 0.7
    shader.inputs['Specular IOR Level'].default_value = 0.08

    camera_image = image.copy()
    camera_image.name = f'{project} camera preview'
    camera_image.colorspace_settings.name = 'AgX Base sRGB'
    camera_image.pack()
    camera_texture = screen.node_tree.nodes.new('ShaderNodeTexImage')
    camera_texture.image = camera_image
    emission = screen.node_tree.nodes.new('ShaderNodeEmission')
    screen.node_tree.links.new(camera_texture.outputs['Color'], emission.inputs['Color'])
    light_path = screen.node_tree.nodes.new('ShaderNodeLightPath')
    camera_surface = screen.node_tree.nodes.new('ShaderNodeMixShader')
    screen.node_tree.links.new(light_path.outputs['Is Camera Ray'], camera_surface.inputs[0])
    screen.node_tree.links.new(shader.outputs['BSDF'], camera_surface.inputs[1])
    screen.node_tree.links.new(emission.outputs['Emission'], camera_surface.inputs[2])
    output = screen.node_tree.nodes.get('Material Output')
    screen.node_tree.links.new(camera_surface.outputs[0], output.inputs['Surface'])

    w = lid_width - 2 * screen_inset
    h = lid_height - 2 * screen_inset
    vertices = [(-w/2, -0.050, screen_inset), (w/2, -0.050, screen_inset),
                (w/2, -0.050, lid_height - screen_inset), (-w/2, -0.050, lid_height - screen_inset)]
    mesh = bpy.data.meshes.new('Display pixels')
    mesh.from_pydata(vertices, [], [(0, 1, 2, 3)])
    mesh.uv_layers.new()
    crop = (0.184, 0.109, 0.688, 0.783) if project == 'forumgw' else (0, 0, 1, 1)
    x, y, cw, ch = crop
    image_ratio = image.size[0] * cw / (image.size[1] * ch)
    screen_ratio = w / h

    if image_ratio > screen_ratio:
        new_width = cw * screen_ratio / image_ratio
        x += (cw - new_width) / 2
        cw = new_width
    else:
        new_height = ch * image_ratio / screen_ratio
        y += ch - new_height
        ch = new_height

    for loop, uv in zip(mesh.uv_layers.active.data, [(x,y), (x+cw,y), (x+cw,y+ch), (x,y+ch)]):
        loop.uv = uv

    display = bpy.data.objects.new('Screenshot display', mesh)
    bpy.context.collection.objects.link(display)
    display.parent = lid
    mesh.materials.append(screen)
    notch_height = 0.075
    notch_center = lid_height - glass_inset - notch_height / 2
    box('Camera notch', location=(0, -0.064, notch_center),
        size=(0.31, 0.019, notch_height), mat=glass, bevel=0.02, parent=lid)
    lens = material('Camera lens', (0.025, 0.040, 0.065), metallic=0.55, roughness=0.14)
    box('FaceTime camera', location=(0, -0.076, notch_center), size=(0.025, 0.008, 0.025), mat=lens, bevel=0.012, parent=lid)

    area('Large softbox', location=(-3.5,-4,6), target=(0,0,1), color=(0.85,0.91,1), energy=420, size=4)
    area('Backdrop wash', location=(-2,0.2,1.7), target=(0,2,2.5), color=light_color, energy=85, size=2)
    area('Edge light', location=(3.5,1.1,4.4), target=(0,0,1.5), color=light_color, energy=280, size=2.3)
    area('Low fill', location=(2,-5,2.2), target=(0,0,1), color=(1,0.85,0.72), energy=45, size=3)

    bpy.ops.object.camera_add(location=(0.4,-8.2,3.0))
    camera = bpy.context.object
    camera.rotation_euler = (Vector((0,0.15,1.65)) - camera.location).to_track_quat('-Z','Y').to_euler()
    camera.data.type = 'PERSP'
    camera.data.lens = 52
    bpy.context.scene.camera = camera
    render = bpy.context.scene
    render.render.engine = 'CYCLES'
    render.cycles.samples = 12 if args.draft else 64
    render.cycles.use_denoising = True
    render.render.resolution_x = 2800
    render.render.resolution_y = 2100
    render.render.resolution_percentage = 50 if args.draft else 100
    render.render.image_settings.file_format = 'PNG'
    render.world.use_nodes = True
    render.world.node_tree.nodes.get('Background').inputs['Color'].default_value = (0.025, 0.025, 0.025, 1)
    render.world.node_tree.nodes.get('Background').inputs['Strength'].default_value = 0.3
    render.view_settings.view_transform = 'AgX'
    output = ROOT / 'static/assets/project-scenes' / f'{project}-macbook.png'
    render.render.filepath = str(output)
    bpy.ops.wm.save_as_mainfile(filepath=str(ROOT / 'design/project-scenes' / f'{project}.blend'))
    bpy.ops.render.render(write_still=True)


for name, colors in PROJECTS.items():
    if args.project and name != args.project:
        continue

    scene(name, colors)
