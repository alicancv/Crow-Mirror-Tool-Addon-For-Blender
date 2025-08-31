import bpy

class HAIR_PT_CreatePanel(bpy.types.Panel):
    bl_label = "Hair Mirror Tool"
    bl_idname = "HAIR_PT_create_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hair Mirror Tool"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "hair_mirror_axis", text="Mirror Axis")

        layout.label(text="Mirror Object:")

        if context.active_object:
            layout.label(text=f"• {context.active_object.name}")
        else:
            layout.label(text="• None")

        layout.operator("hair.create_hair", text="Create Hair")

def register():
    bpy.utils.register_class(HAIR_PT_CreatePanel)

def unregister():
    try:
        bpy.utils.unregister_class(HAIR_PT_CreatePanel)
    except RuntimeError:
        print(f"[WARN] {HAIR_PT_CreatePanel.__name__} was not registered.")