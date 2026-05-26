import numpy as np


def rotation_z(theta):
    """
    Creates a 3x3 rotation matrix around the Z axis.
    """

    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])