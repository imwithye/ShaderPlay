from PIL import Image
from numpy import floor, mod
from tqdm import tqdm
from .mathtypes import vec2, vec4
from .mathfuncs import saturate


class RenderContext:
    def __init__(self, iResolution):
        self.iResolution = iResolution
        self.fragCoord = vec2(0)
        self.fragColor = vec4(0)


def render(shader, size=(256, 256), mode="RGB", show_progress=True):
    image = Image.new(mode, size)
    ctx = RenderContext(vec2(size[0], size[1]))
    r = range(0, size[0]*size[1])
    for uv in (tqdm(r) if show_progress else r):
        x = int(floor(uv / size[1]))
        y = int(mod(uv, size[1]))
        ctx.fragCoord = vec2(x+0.5, size[1]-y+0.5)
        ctx.fragColor = vec4(0)
        shader.mainImage(ctx)
        ctx.fragColor = saturate(ctx.fragColor)
        color = tuple([int(c * 255) for c in ctx.fragColor])
        image.putpixel((x, y), color)
    return image
