import bpy

class MESH_PT_MirrorPanel(bpy.types.Panel):
    bl_label = "Mesh Mirror Tool"
    bl_idname = "MESH_PT_mirror_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Mesh Mirror Tool"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout    
        scene = context.scene  

        layout.prop(scene, "mesh_mirror_axis", text="Mirror Axis")

        layout.label(text="Selected Meshes:")
        box = layout.box()
        
        selected_names = list(context.scene.get("mirror_last_selected_meshes", []))
    
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

        layout.operator("mesh.mirror_mesh", text="Mirror Meshes")

classes = [MESH_PT_MirrorPanel]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            print(f"[WARN] {cls.__name__} was not registered.")