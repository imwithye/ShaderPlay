import numpy as np
from numpy import clip as clamp
from numpy import floor, ceil, sin, cos, tan, mod


def saturate(vec):
    return clamp(vec, 0.0, 1.0)


def mix(v1, v2, a):
    return v1 * (1-a) + v2 * a
