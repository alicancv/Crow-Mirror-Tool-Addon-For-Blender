import bpy
from .as_utils import TransformToolkit 

def mirror_curve_across_object(curve_object, mirror_object, axis='X'):     
    if not curve_object or not mirror_object:
        print("[ERROR] Object(s) not found.")
        return
    
    if curve_object.type != "CURVE":
        print("[ERROR] Source must be a curve object.")
        return
    
    mirrored_curve = curve_object.copy()
    mirrored_curve.data = curve_object.data.copy()
    mirrored_curve.animation_data_clear()
    mirrored_curve.data.use_fake_user = True    
    mirrored_curve.name = curve_object.name + "_mirrored"
    # bpy.context.collection.objects.link(mirrored_curve)
    curve_object.users_collection[0].objects.link(mirrored_curve)

    mirror_matrix = TransformToolkit.mirror_matrix(mirror_object.matrix_world, axis)

    mirrored_curve.matrix_world = mirror_matrix @ mirrored_curve.matrix_world 

    print(f"[SUCCESS] Curve '{curve_object.name}' mirrored across '{mirror_object.name}' on '{axis}' axis.")
    return mirrored_curve