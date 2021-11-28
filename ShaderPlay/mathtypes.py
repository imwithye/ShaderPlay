import numba as nb
import numpy as np


class VectorImpl(np.ndarray):
    def __new__(cls, dim, *args):
        ret = np.array([])
        for arg in args:
            ret = np.append(ret, arg if np.isscalar(arg) else arg.flatten())
        assert len(ret) == 1 or len(ret) == dim
        if len(ret) == 1:
            ret = np.ones(dim) * ret[0]
        return ret.view(VectorImpl)

    def swizzle_indices(self, attrs):
        index = {"x": 0, "y": 1, "z": 2, "w": 3,
                 "r": 0, "g": 1, "b": 2, "a": 3}
        return [index[a] for a in attrs]

    def __getattr__(self, attrs):
        indices = self.swizzle_indices(attrs)
        values = np.array([self[i] for i in indices])
        return values[0] if len(attrs) == 1 else VectorImpl(len(values), values)

    def __setattr__(self, attrs, vals):
        indices = self.swizzle_indices(attrs)
        if np.isscalar(vals):
            vals = np.array(vals)
        assert len(indices) == len(vals)
        for idx, i in enumerate(indices):
            self[i] = vals[idx]


def vec2(*args):
    return VectorImpl(2, *args)


def vec3(*args):
    return VectorImpl(3, *args)


def vec4(*args):
    return VectorImpl(4, *args)
