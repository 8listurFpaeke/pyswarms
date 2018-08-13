#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fixtures for tests"""

# Import modules
import pytest
import numpy as np

# Import from package
from pyswarms.backend.swarms import Swarm


@pytest.fixture(scope="module")
def swarm():
    """A contrived instance of the Swarm class at a certain timestep"""
    attrs_at_t = {
        "position": np.array([[9.95838686e-01,  5.87433429e-04,  6.49113772e-03],
                             [1.00559609e+00,   3.96477697e-02,  7.67205397e-01],
                             [2.87990950e-01,  -3.64932609e-02,  1.89750725e-02],
                             [1.11646877e+00,   3.12037361e-03,  1.97885369e-01],
                             [8.96117216e-01,  -9.79602053e-03, -1.66139336e-01],
                             [9.90423669e-01,   1.99307974e-03, -1.23386797e-02],
                             [2.06800701e-01,  -1.67869387e-02,  1.14268810e-01],
                             [4.21786494e-01,   2.58755510e-02,  6.62254843e-01],
                             [9.90350831e-01,   3.81575154e-03,  8.80833545e-01],
                             [9.94353749e-01,  -4.85086205e-02,  9.85313500e-03]]),
        "velocity": np.array([[2.09076818e-02,  2.04936403e-03,  1.06761248e-02],
                             [1.64940497e-03,  5.67924469e-03, 9.74902301e-02],
                             [1.50445516e-01, 9.11699158e-03,  1.51474794e-02],
                             [2.94238740e-01,   5.71545680e-04, 1.54122294e-02],
                             [4.10430034e-02,  6.51847479e-04, 6.25109226e-02],
                             [6.71076116e-06, 1.89615516e-04, 4.65023770e-03],
                             [4.76081378e-02,  4.24416089e-03, 7.11856172e-02],
                             [1.33832808e-01,  1.81818698e-02,  1.16947941e-01],
                             [1.22849955e-03,  1.55685312e-03, 1.67819003e-02],
                             [5.60617396e-03, 4.31819608e-02,  2.52217220e-02]]),
        "current_cost": np.array([1.07818462,  5.5647911,  19.6046078,  14.05300016,  3.72597614,  1.01169386,
                                  16.51846203, 32.72262829,  3.80274901,  1.05237138]),
        "pbest_cost": np.array([1.00362006, 2.39151041, 2.55208424, 5.00176207, 1.04510827, 1.00025284,
                                6.31216654, 2.53873121, 2.00530884, 1.05237138]),
        "pbest_pos": np.array([[9.98033031e-01,  4.97392619e-03,  3.07726256e-03],
                               [1.00665809e+00,  4.22504014e-02,  9.84334657e-01],
                               [1.12159389e-02,  1.11429739e-01,  2.86388193e-02],
                               [1.64059236e-01,  6.85791237e-03, -2.32137604e-02],
                               [9.93740665e-01, -6.16501403e-03, -1.46096578e-02],
                               [9.90438476e-01,  2.50379538e-03,  1.87405987e-05],
                               [1.12301876e-01,  1.77099784e-03,  1.45382457e-01],
                               [4.41204876e-02,  4.84059652e-02,  1.05454822e+00],
                               [9.89348409e-01, -1.31692358e-03,  9.88291764e-01],
                               [9.99959923e-01, -5.32665972e-03, -1.53685870e-02]]),
        "best_cost": 1.0002528364353296,
        "best_pos": np.array([9.90438476e-01, 2.50379538e-03, 1.87405987e-05]),
        "options": {'c1': 0.5, 'c2': 0.3, 'w': 0.9},
    }
    return Swarm(**attrs_at_t)