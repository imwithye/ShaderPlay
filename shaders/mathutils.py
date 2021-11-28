import numpy as np


class __vec__(object):
    def __init__(self, values):
        self._values = np.array(values)

    def __getattr__(self, attrs):
        if not _is_swizzle_attrs(attrs):
            return self.__dict__[attrs]
        indices = _swizzle_indices(attrs)
        values = [self._values[i] for i in indices]
        if len(attrs) == 1:
            return values[0]
        if len(attrs) == 2:
            return vec2(values)
        if len(attrs) == 3:
            return vec3(values)
        if len(attrs) == 3:
            return vec4(values)

    def __setattr__(self, attrs, value):
        if not _is_swizzle_attrs(attrs):
            self.__dict__[attrs] = value
            return
        indices = _swizzle_indices(attrs)
        values = _list_of(value)
        for i in indices:
            self._values[i] = values[i]

    def __len__(self):
        return len(self._values)

    def __getitem__(self, idx):
        return self._values[idx]

    def __setitem__(self, idx, value):
        self._values[idx] = value

    def __iter__(self):
        return self._values.__iter__()

    def __str__(self):
        s = [str(v) for v in self._values]
        return f"({', '.join(s)})"

    def __repr__(self):
        return self.__str__()

    def clamp(self, min=0.0, max=1.0):
        return __vec__(self._values.clip(min, max))


class vec2(__vec__):
    def __init__(self, *args):
        super().__init__(flatten(args, 2))


class vec3(__vec__):
    def __init__(self, *args):
        super().__init__(flatten(args, 3))


class vec4(__vec__):
    def __init__(self, *args):
        super().__init__(flatten(args, 4))


def flatten(args, length):
    lists = [_list_of(y) for y in args]
    values = [float(item) for sub in lists for item in sub]
    for i in range(len(values), length):
        values.append(0.0)
    return values[0:length]


def _list_of(val):
    if getattr(val, "__iter__", None) is None:
        return [val]
    return [v for v in val]


def _is_swizzle_attrs(attrs):
    for i in attrs:
        if i not in ["x", "y", "z", "w", "r", "g", "b", "a"]:
            return False
    return True


def _swizzle_indices(attrs):
    assert _is_swizzle_attrs(attrs)
    index = {"x": 0, "y": 1, "z": 2, "w": 3, "r": 0, "g": 1, "b": 2, "a": 3}
    return [index[a] for a in attrs]
