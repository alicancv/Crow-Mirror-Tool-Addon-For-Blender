import bpy
from .mesh_mirror_utils import mirror_mesh_across_object
from .curve_mirror_utils import mirror_curve_across_object

def hair_full_from_half(mirror_object, axis = "X"):
    if not mirror_object:
        print("[ERROR] No Mirror Object Provided")
        return False

    objects = bpy.data.objects
    
    mesh_suffix = "_hairmesh"
    # curve_suffix = "_haircurve"

    original_meshes = [obj for obj in objects if obj.type == "MESH" and obj.name.endswith(mesh_suffix)]
    if not original_meshes:
        print("[ERROR] Hair object(s) not found.")
        return False
    else:
        for mesh in original_meshes:           
            # mesh_base_name = mesh.name[:-len(mesh_suffix)]
            # meshs_curve = objects.get(mesh_base_name + curve_suffix)

            if "Mirror" in mesh.modifiers:
                mesh.modifiers.remove(mesh.modifiers["Mirror"])

            try: 
                meshs_curve_mod = mesh.modifiers["Curve"]
                meshs_curve = meshs_curve_mod.object
                
                mesh_mirrored = mirror_mesh_across_object(mesh, mirror_object, axis)
                meshs_curve_mirrored = mirror_curve_across_object(meshs_curve, mirror_object, axis)
                mesh_mirrored.modifiers["Curve"].object = meshs_curve_mirrored
            except KeyError:
                print(f"[ERROR] Hair object {mesh.name} should have curve modifier with appropriate curve object")
    
    return True