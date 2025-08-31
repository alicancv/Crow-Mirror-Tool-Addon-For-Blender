from mathutils import Matrix, Vector, Euler, Quaternion

class TransformToolkit:
    @staticmethod
    def build_matrix(location, rotation_euler, scale):
        """
        Builds a 4x4 transformation matrix from location, Euler rotation, and scale.
        """
        translation_matrix = Matrix.Translation(location)
        rotation_matrix = rotation_euler.to_matrix().to_4x4()
        scale_matrix = Matrix.Diagonal(scale).to_4x4()
        return translation_matrix @ rotation_matrix @ scale_matrix

    @staticmethod
    def decompose_matrix(matrix):
        """
        Decomposes a 4x4 matrix into location, quaternion rotation, and scale.
        """
        loc, rot_quat, scale = matrix.decompose()
        rot_euler = rot_quat.to_euler('XYZ')
        return loc, rot_euler, scale

    @staticmethod
    def mirror_matrix(matrix, axis='X'):
        """
        Mirrors a transformation matrix across the specified axis.
        Axis can be 'X', 'Y', or 'Z'.
        """
        mirror_vec = {
            'X': Vector((-1, 1, 1)),
            'Y': Vector((1, -1, 1)),
            'Z': Vector((1, 1, -1))
        }.get(axis.upper(), Vector((1, 1, 1)))

        scale_matrix = Matrix.Diagonal(mirror_vec).to_4x4()
        return scale_matrix @ matrix 

    @staticmethod
    def flip_local_axis(obj, axis='X'):
        """
        Flips the object's local axis by applying a negative scale.
        """
        axis_map = {"X": 0, "Y": 1, "Z": 2}
        axis_index = axis_map.get(axis.upper(), 0)
    
        obj.scale[axis_index] *= -1

        # bpy.context.view_layer.objects.active = obj
        # bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

        # flip_vec = {
        #     'X': Vector((-1, 1, 1)),
        #     'Y': Vector((1, -1, 1)),
        #     'Z': Vector((1, 1, -1))
        # }.get(axis.upper(), Vector((1, 1, 1)))

        # obj.scale = Vector(obj.scale) * flip_vec

    @staticmethod
    def align_matrix(obj, target, offset=Vector((0, 0, 0))):
        """
        Aligns obj's transform to target's transform, with optional offset.
        """
        target_matrix = target.matrix_world.copy()
        obj.matrix_world = target_matrix @ Matrix.Translation(offset)

    @staticmethod
    def detect_mirror_axis(obj_a, obj_b):
        """
        Detects the most likely mirror axis between two objects based on bounding box symmetry.
        Returns 'X', 'Y', or 'Z'.
        """
        bb_a = [obj_a.matrix_world @ Vector(corner) for corner in obj_a.bound_box]
        bb_b = [obj_b.matrix_world @ Vector(corner) for corner in obj_b.bound_box]

        def get_center(bb):
            min_corner = Vector((min(v[i] for v in bb) for i in range(3)))
            max_corner = Vector((max(v[i] for v in bb) for i in range(3)))
            return (min_corner + max_corner) / 2

        center_a = get_center(bb_a)
        center_b = get_center(bb_b)
        delta = center_b - center_a

        axis_index = max(range(3), key=lambda i: abs(delta[i]))
        return ['X', 'Y', 'Z'][axis_index]
    
    @staticmethod
    def align_curve_to_original(mirrored_curve, original_curve, axis='X'):
        """
        Aligns mirrored curve's origin and scale to match the original curve.
        Also flips tilt and handles if needed.
        """
        mirrored_curve.location = original_curve.location.copy()
        mirrored_curve.scale = original_curve.scale.copy()

        for spline_m, spline_o in zip(mirrored_curve.data.splines, original_curve.data.splines):
            if spline_m.type == 'BEZIER' and spline_o.type == 'BEZIER':
                for bp_m, bp_o in zip(spline_m.bezier_points, spline_o.bezier_points):
                    bp_m.tilt = -bp_o.tilt
                    bp_m.radius = bp_o.radius
            else:
                for pt_m, pt_o in zip(spline_m.points, spline_o.points):
                    pt_m.tilt = -pt_o.tilt
                    pt_m.radius = pt_o.radius
                    pt_m.weight = pt_o.weight