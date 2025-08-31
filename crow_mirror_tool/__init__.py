bl_info = {
    "name": "Crow Mirror Addon",
    "author": "Alican Sucu",
    "version": (1, 0),
    "blender": (4, 5, 1),
    "location": "View3D > Sidebar > Mirror Tools",
    "description": "Mirrors meshes and curves across a target object",
    "category": "Object",
}

print("Initializing Crow Mirror Addon")

import importlib
from . import as_utils, properties, ui_utils
from . import curve_mirror_utils, curve_ui_operator, curve_ui_panel
from . import mesh_mirror_utils,  mesh_ui_operator, mesh_ui_panel
from . import hair_create_utils, hair_ui_operator, hair_ui_panel

modules = [as_utils, 
           curve_mirror_utils, curve_ui_operator, curve_ui_panel,
           mesh_mirror_utils, mesh_ui_operator, mesh_ui_panel, 
           hair_create_utils, hair_ui_operator, hair_ui_panel,
           properties, ui_utils]

for mod in modules:
    importlib.reload(mod)

def register():
    for mod in modules:
        if hasattr(mod, "register"):
            mod.register()

def unregister():
    for mod in reversed(modules):
        if hasattr(mod, "unregister"):
            mod.unregister()