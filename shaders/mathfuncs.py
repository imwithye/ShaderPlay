from .mathutils import __vec__


def clamp(val, min=0.0, max=0.0):
    if not isinstance(val, __vec__):
        val = min if val < min else val
        val = max if val > max else max
        return val
    return val.clamp(min, max)


def saturate(val):
    return clamp(val, 0.0, 1.0)
