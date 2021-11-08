import numpy as np
from renderer import Renderer
from shaders import *
import moderngl
import colorsys
import math

class TestRenderer(Renderer):

    def main(self):
        self.prog = self.ctx.program(vertex_shader=vertex_shader_source_unlit, fragment_shader=fragment_shader_source_unlit)
        self.prog_mvp = self.prog['modelViewProj']
        self.prog_color = self.prog['color']

        vertices = np.array([
                 0.0,  0.0, 0.0,
                30.0,  0.0, 0.0,
                30.0, 30.0, 0.0,
            ], dtype='f4')

        self.vbo = self.ctx.buffer(vertices)
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, 'position')
        self.hue = 0.0

        self.run()

    def on_draw(self, ctx, dt):
        self.hue = math.fmod(self.hue + dt * 0.1, 1.0)
        color = colorsys.hsv_to_rgb(self.hue, 1.0, 0.5)

        self.prog_mvp.write(self.modelViewProjection.astype('f4').tobytes())
        self.prog_color.write(np.array(color, dtype='f4').tobytes())
        self.vao.render(moderngl.TRIANGLES)

if __name__ == "__main__":
    TestRenderer().main()
