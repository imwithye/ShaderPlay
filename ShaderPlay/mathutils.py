class __vec__(object):
    def __init__(self, values):
        self._values = values

    def __getattr__(self, attrs):
        if not _is_swizzle_attrs(attrs):
            return self.__dict__[attrs]
        indices = _swizzle_indices(attrs)
        values = [self._values[i] for i in indices]
        if len(attrs) == 1:
            return values[0]
        return vec(values)

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

    def __custom_op__(self, val, op):
        length = len(self._values)
        assert length == 2 or length == 3 or length == 4
        if not isinstance(val, __vec__):
            val = [val for i in range(0, length)]
        values = [op(self[i], val[i]) for i in range(0, length)]
        return vec(values)

    def __add__(self, val):
        return self.__custom_op__(val, lambda a, b: a+b)

    def __radd__(self, val):
        return self.__custom_op__(val, lambda a, b: a+b)

    def __sub__(self, val):
        return self.__custom_op__(val, lambda a, b: a-b)

    def __rsub__(self, val):
        return self.__custom_op__(val, lambda a, b: b-a)

    def __mul__(self, val):
        return self.__custom_op__(val, lambda a, b: a*b)

    def __rmul__(self, val):
        return self.__custom_op__(val, lambda a, b: a*b)

    def __truediv__(self, val):
        return self.__custom_op__(val, lambda a, b: a/b)

    def clamp(self, min=0.0, max=1.0):
        values = []
        for v in self._values:
            v = min if v < min else v
            v = max if v > max else v
            values.append(v)
        return vec(values)


class vec2(__vec__):
    def __init__(self, *args):
        super().__init__(flatten(args, 2))


class vec3(__vec__):
    def __init__(self, *args):
        super().__init__(flatten(args, 3))


class vec4(__vec__):
    def __init__(self, *args):
        super().__init__(flatten(args, 4))


def vec(values):
    assert len(values) in [2, 3, 4]
    if len(values) == 2:
        return vec2(values)
    if len(values) == 3:
        return vec3(values)
    if len(values) == 4:
        return vec4(values)


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
