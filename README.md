# Crow-Mirror-Tool-Addon-For-Blender
A mirror tool (addon) for Blender. It is used for mirroring curves and meshes. When it mirrors it also mirrors origin of the object providing a consitent mirroring for both meshes and curves. It also has hair mirror tool.

# Mesh and Curve Mirroring
https://github.com/user-attachments/assets/2669e18d-5361-453b-8ff9-c1241562038c

# Hair Tool
https://github.com/user-attachments/assets/70a022f8-7810-47ed-be9d-8aa56b21ddb2

# Notes
- Hair meshes' name should be postfixed with "_hairmesh" and hair meshes' should have a curve modifier with a curve assigned to it.
- Hair curves' name postfixed with "_haircurve" is a good practice
- If tools' ui doesn't work properly just reload the addon
```
import importlib
import crow_mirror_tool

importlib.reload(crow_mirror_tool)
crow_mirror_tool.unregister()
crow_mirror_tool.register()
```
