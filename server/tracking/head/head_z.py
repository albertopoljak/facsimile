__all__ = ('get_head_z_rotation',)

from math import atan2, tau

from ..face_mesh_points import FACE_MESH_POINT__FOREHEAD__LEFT, FACE_MESH_POINT__FOREHEAD__RIGHT


def get_head_z_rotation(landmarks):
    right = landmarks[FACE_MESH_POINT__FOREHEAD__RIGHT]
    left = landmarks[FACE_MESH_POINT__FOREHEAD__LEFT]
    
    return atan2(left.y - right.y, left.x - right.x) * 180.0 / tau
