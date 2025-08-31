import bpy

properties = {
    "curve_mirror_axis": bpy.props.EnumProperty(
        name="Axis",
        items=[('X', "X", ""), ('Y', "Y", ""), ('Z', "Z", "")]
    ),
    "mesh_mirror_axis": bpy.props.EnumProperty(
        name="Axis",
        items=[('X', "X", ""), ('Y', "Y", ""), ('Z', "Z", "")]
    ),
    "hair_mirror_axis" : bpy.props.EnumProperty(
        name="Axis",
        items=[('X', "X", ""), ('Y', "Y", ""), ('Z', "Z", "")]
    )
}

def register():
    for name, prop in properties.items():
        setattr(bpy.types.Scene, name, prop)

def unregister():
    for name in properties:
        if hasattr(bpy.types.Scene, name):
            delattr(bpy.types.Scene, name)