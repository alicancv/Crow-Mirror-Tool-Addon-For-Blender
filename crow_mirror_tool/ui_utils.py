import bpy
from .mesh_ui_panel import MESH_PT_MirrorPanel
from .curve_ui_panel import CURVE_PT_MirrorPanel

addon_running = True

def redraw_timer():
    if not addon_running:
        return None

    panel_list = [CURVE_PT_MirrorPanel, MESH_PT_MirrorPanel]

    redraw_visible_panels(bpy.context, panel_list)
    return 0.5

def redraw_visible_panels(context, panel_classes):
    for window in context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type != 'VIEW_3D':
                continue

            space = area.spaces.active
            if not space.show_region_ui:
                continue 

            for region in area.regions:
                if region.type == 'UI':
                    for panel_class in panel_classes:
                        if panel_class.poll(context):
                            curve_selection_handler(context)
                            mesh_selection_handler(context)
                            area.tag_redraw()
                        break

def curve_selection_handler(context):
    property_name = "mirror_last_selected_curves"

    selected_curves = [obj.name for obj in context.selected_objects if obj.type == "CURVE" and obj != context.active_object]
    last_selected = list(context.scene.get(property_name, []))
    
    if selected_curves != last_selected:
        context.scene[property_name] = selected_curves
        print(f"[DEBUG] Updated selected curves: {selected_curves}")

def mesh_selection_handler(context):
    property_name = "mirror_last_selected_meshes"

    selected_meshes = [obj.name for obj in context.selected_objects if obj.type == "MESH" and obj != context.active_object]    
    last_selected = list(context.scene.get(property_name, []))

    if selected_meshes != last_selected:
        context.scene[property_name] = selected_meshes
        print(f"[DEBUG] Updated selected meshes: {selected_meshes}")

def register():
    global addon_running
    addon_running = True
    bpy.app.timers.register(redraw_timer)

def unregister():
    global addon_running
    addon_running = False