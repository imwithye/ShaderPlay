from PIL import Image
from .shader import Context
from .mathutils import vec2, vec4
from .mathfuncs import saturate


def draw(shader, size=(256, 256), mode="RGB"):
    image = Image.new(mode, size)
    ctx = Context(vec2(size))
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            # range from 0.5 to resolution-0.5
            ctx.fragCoord = vec2(x+0.5, size[1]-y+0.5)
            ctx.fragColor = vec4()
            shader.mainImage(ctx)
            ctx.fragColor = saturate(ctx.fragColor)
            color = tuple([int(c * 255) for c in ctx.fragColor])
            image.putpixel((x, y), color)
    return image
