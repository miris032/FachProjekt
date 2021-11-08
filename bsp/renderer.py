import numpy as np
import glfw
import moderngl
from pyrr import Matrix44, Matrix33

class Renderer:
    def __init__(self):
        if not glfw.init():
            raise('Could not initialize GLFW')
        self.window = glfw.create_window(640, 480, "Hello World", None, None)
        if not self.window:
            glfw.terminate()
            raise('Could not create rendering window')

        glfw.make_context_current(self.window)
        self.ctx = moderngl.create_context()


    def run(self):
        last_time = glfw.get_time()
        while not glfw.window_should_close(self.window):
            current_time = glfw.get_time()
            delta_time = current_time - last_time
            last_time = current_time

            self.buffer_width, self.buffer_height = glfw.get_framebuffer_size(self.window)
            self.ctx.viewport = (0, 0, self.buffer_width, self.buffer_height)

            proj = Matrix44.perspective_projection(80.0, self.buffer_width/self.buffer_height, 0.1, 1000.0)
            lookat = Matrix44.look_at(
                (50.0, 50.0, 50.0),
                (0.0, 0.0, 0.0),
                (0.0, 0.0, 1.0),
            )
            self.modelViewProjection = proj * lookat
            self.normalMatrix = Matrix33.from_matrix44(lookat).inverse.transpose()

            self.ctx.clear(0.1, 0.15, 0.2, 0.0)
            self.ctx.enable(moderngl.DEPTH_TEST)
            self.on_draw(self.ctx, delta_time)

            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.terminate()

    def on_draw(self, ctx, dt):
        pass
