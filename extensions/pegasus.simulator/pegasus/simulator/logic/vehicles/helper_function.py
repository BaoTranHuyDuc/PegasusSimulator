import numpy as np

def quat_to_rotation_matrix(quat):
    """
    Converts a quaternion [qx, qy, qz, qw] into a 3x3 rotation matrix.
    """
    qx, qy, qz, qw = quat
    
    # Pre-calculate products for efficiency
    sqw = qw**2
    sqx = qx**2
    sqy = qy**2
    sqz = qz**2

    # Calculate the matrix elements
    r00 = sqx - sqy - sqz + sqw
    r11 = -sqx + sqy - sqz + sqw
    r22 = -sqx - sqy + sqz + sqw

    tmp1 = qx * qy
    tmp2 = qz * qw
    r10 = 2.0 * (tmp1 + tmp2)
    r01 = 2.0 * (tmp1 - tmp2)

    tmp1 = qx * qz
    tmp2 = qy * qw
    r20 = 2.0 * (tmp1 - tmp2)
    r02 = 2.0 * (tmp1 + tmp2)

    tmp1 = qy * qz
    tmp2 = qx * qw
    r21 = 2.0 * (tmp1 + tmp2)
    r12 = 2.0 * (tmp1 - tmp2)

    return np.array([
        [r00, r01, r02],
        [r10, r11, r12],
        [r20, r21, r22]
    ])