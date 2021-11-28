from .mathtypes import vec4


class ImageShader:
    def mainImage(self, ctx):
        ctx.fragColor = vec4(0, 0, 0, 0)
