import bpy
from .as_utils import TransformToolkit 
    
def mirror_mesh_across_object(mesh_object, mirror_object, axis='X'):     
    if not mesh_object or not mirror_object:
        print("[ERROR] Object(s) not found.")
        return
    
    if mesh_object.type != "MESH":
        print("[ERROR] Source must be a mesh object.")
        return
    
    mirrored_mesh = mesh_object.copy()
    mirrored_mesh.data = mesh_object.data.copy()
    mirrored_mesh.animation_data_clear()
    mirrored_mesh.data.use_fake_user = True    
    mirrored_mesh.name = mesh_object.name + "_mirrored"
    # bpy.context.collection.objects.link(mirrored_mesh)
    mesh_object.users_collection[0].objects.link(mirrored_mesh)

    mirror_matrix = TransformToolkit.mirror_matrix(mirror_object.matrix_world, axis)

    mirrored_mesh.matrix_world = mirror_matrix @ mirrored_mesh.matrix_world 
        
    print(f"[SUCCESS] Mesh '{mesh_object.name}' mirrored across '{mirror_object.name}' on {axis} axis.")
    return mirrored_mesh