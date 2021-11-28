import math
from .mathutils import __vec__, vec


def clamp(val, min=0.0, max=0.0):
    if not isinstance(val, __vec__):
        val = min if val < min else val
        val = max if val > max else max
        return val
    return val.clamp(min, max)


def saturate(val):
    return clamp(val, 0.0, 1.0)


def floor(val):
    if not isinstance(val, __vec__):
        return math.floor(val)
    return vec([math.floor(i) for i in val])


def ceil(val):
    if not isinstance(val, __vec__):
        return math.ceil(val)
    return vec([math.ceil(i) for i in val])


def mod(v1, v2):
    return v1 - v2 * floor(v1 / v2)


def mix(v1, v2, a):
    return v1 * (1-a) + v2 * a


def absolute(val):
    if not isinstance(val, __vec__):
        return abs(val)
    return vec([abs(i) for i in val])


def sin(val):
    if not isinstance(val, __vec__):
        return math.sin(val)
    return vec([math.sin(i) for i in val])


def cos(val):
    if not isinstance(val, __vec__):
        return math.cos(val)
    return vec([math.cos(i) for i in val])


def tan(val):
    if not isinstance(val, __vec__):
        return math.tan(val)
    return vec([math.tan(i) for i in val])
