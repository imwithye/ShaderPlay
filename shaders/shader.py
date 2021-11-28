from .mathutils import vec2, vec3, vec4


class Context:
    def __init__(self, iResolution):
        self.iResolution = iResolution
        self.iFrame = int(0)
        self.fragCoord = vec2()
        self.fragColor = vec4()


class ImageShader:
    def mainImage(self, ctx):
        ctx.fragColor = vec4(0, 0, 0, 0)
