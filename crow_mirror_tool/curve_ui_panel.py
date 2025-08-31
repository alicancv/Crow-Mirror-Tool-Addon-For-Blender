import bpy

class CURVE_PT_MirrorPanel(bpy.types.Panel):
    bl_label = "Curve Mirror Tool"
    bl_idname = "CURVE_PT_mirror_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Curve Mirror Tool"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout    
        scene = context.scene  

        layout.prop(scene, "curve_mirror_axis", text="Mirror Axis")

        layout.label(text="Selected Curves:")
        box = layout.box()
        
        selected_names = list(context.scene.get("mirror_last_selected_curves", []))
    
        if not selected_names:
            box.label(text="• None")
        else:
            max_display = 10
            for name in selected_names[:max_display]:
                box.label(text=f"• {name}")
            if len(selected_names) > max_display:
                box.label(text=f"...and {len(selected_names) - max_display} more")

        layout.label(text="Mirror Object:")

        if context.active_object:
            layout.label(text=f"• {context.active_object.name}")
        else:
            layout.label(text="• None")

        layout.operator("curve.mirror_curve", text="Mirror Curves")

def register():
    bpy.utils.register_class(CURVE_PT_MirrorPanel)

def unregister():
    try:
        bpy.utils.unregister_class(CURVE_PT_MirrorPanel)
    except RuntimeError:
            print(f"[WARN] {CURVE_PT_MirrorPanel.__name__} was not registered.")