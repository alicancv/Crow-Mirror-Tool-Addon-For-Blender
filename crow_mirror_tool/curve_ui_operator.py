import bpy
from .curve_mirror_utils import mirror_curve_across_object

class CURVE_OT_MirrorCurve(bpy.types.Operator):
    bl_idname = "curve.mirror_curve"
    bl_label = "Mirror Curve"
    bl_description = "Mirrors selected curves across the active object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        mirror_obj = context.active_object
        selected_curves = [obj for obj in context.selected_objects if obj.type == "CURVE" and obj != mirror_obj]
        curve_mirror_axis = context.scene.curve_mirror_axis
        
        if not selected_curves:
            self.report({'ERROR'}, "No curve objects selected.")
            return {'CANCELLED'}

        if not mirror_obj:
            self.report({'ERROR'}, "No mirror object selected.")
            return {'CANCELLED'}

        for curve_obj in selected_curves:
            mirror_curve_across_object(curve_obj, mirror_obj, curve_mirror_axis)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(CURVE_OT_MirrorCurve)

def unregister():
    try:
        bpy.utils.unregister_class(CURVE_OT_MirrorCurve)
    except RuntimeError:
            print(f"[WARN] {CURVE_OT_MirrorCurve.__name__} was not registered.")