from importlib.util import set_loader
import glm
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader


class Renderer:
    """openGL renderer with opengl and pygame"""
    def __init__(self, screen) -> None:
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()

        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.width, self.height)

    def render(self):
        glClearColor(0.2,0.2,0.3,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
