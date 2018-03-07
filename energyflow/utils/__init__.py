"""A subpackage containing utility functions and classes."""

from __future__ import absolute_import

import os

import numpy as np

from . import events
from . import graph

from .events import *
from .graph import *

# concatenates con. and disc. specs along axis 0, handling empty disc. specs
def concat_specs(c_specs, d_specs):
    if len(d_specs):
        return np.concatenate((c_specs, d_specs), axis=0)
    else:
        return c_specs

def transfer(obj1, obj2, attrs):
    if isinstance(obj2, dict):
        for attr in attrs:
            setattr(obj1, attr, obj2[attr])
    else:
        for attr in attrs:
            setattr(obj1, attr, getattr(obj2, attr))

ef_data_dir = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
default_efp_file = os.path.join(ef_data_dir, 'efps_d_le_9.npz')

__all__ = events.__all__
