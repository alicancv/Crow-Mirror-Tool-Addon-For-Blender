import bpy
from .mesh_mirror_utils import mirror_mesh_across_object

class MESH_OT_MirrorMesh(bpy.types.Operator):
    bl_idname = "mesh.mirror_mesh"
    bl_label = "Mirror Mesh"
    bl_description = "Mirrors selected meshes across the active object"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        mirror_obj = context.active_object
        selected_meshes = [obj for obj in context.selected_objects if obj.type == "MESH" and obj != mirror_obj]
        mesh_mirror_axis = context.scene.mesh_mirror_axis
        
        if not selected_meshes:
            self.report({'ERROR'}, "No mesh objects selected.")
            return {'CANCELLED'}

        if not mirror_obj:
            self.report({'ERROR'}, "No mirror object selected.")
            return {'CANCELLED'}

        for mesh_obj in selected_meshes:
            mirror_mesh_across_object(mesh_obj, mirror_obj, mesh_mirror_axis)

        return {'FINISHED'}

classes = [MESH_OT_MirrorMesh]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            print(f"[WARN] {cls.__name__} was not registered.")