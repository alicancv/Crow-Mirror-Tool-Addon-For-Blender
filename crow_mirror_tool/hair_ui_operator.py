import bpy
from .hair_create_utils import hair_full_from_half

class HAIR_OT_CreateHair(bpy.types.Operator):
    bl_idname = "hair.create_hair"
    bl_label = "Hair Create"
    bl_description = "Provide half of the hair meshes and curves to complete full hair"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        hair_mirror_axis = context.scene.hair_mirror_axis
        mirror_obj = context.active_object
        result = hair_full_from_half(mirror_obj, hair_mirror_axis)
        
        if not result:
            self.report({'ERROR'}, "Hair creation could not be completed")
            return {'CANCELLED'}

        return {'FINISHED'}

def register():
    bpy.utils.register_class(HAIR_OT_CreateHair)

def unregister():
    try:
        bpy.utils.unregister_class(HAIR_OT_CreateHair)
    except RuntimeError:
        print(f"[WARN] {HAIR_OT_CreateHair.__name__} was not registered.")