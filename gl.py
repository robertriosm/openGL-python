
from glm import vec3
import glm
from numpy import array, float32
from OpenGL.GL import *
from ctypes import c_void_p
from OpenGL.GL.shaders import compileProgram, compileShader
from shaders import * 




class Buffer:
    """buffer class to generate objects"""
    def __init__(self, data) -> None:
        self.data = data
        self.createVertexBuffer()

        self.createVertexBuffer()

        self.position = vec3(0,0,0)

        self.rotation = vec(0,0,0)

        self.


    def createVertexBuffer(self):
        self.vertBuffer = array(self.data, dtype=float32)
        #vertex buffer object
        self.VBO = glGenBuffers(1)
        #vertex array object
        self.VAO = glGenVertexArrays(1)



    def render(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.VAO)
        glBindVertexArray(self.VAO)

        # send vertex info:
        # buffer id (especifica de que modo se le envia la info al buffer) 
        # buffer size
        # buffer data 
        # usage
        glBufferData(GL_ARRAY_BUFFER, self.vertBuffer.nbytes, self.vertBuffer, GL_STATIC_DRAW)

        # attrs:

        # positions

        # attr number
        # size = 3
        # type
        # is normalized
        # stride
        # offset   (usando punteros de C)
        glVertexAttribLPointer(0,3,GL_FLOAT,GL_FALSE, 4 * 6, c_void_p(0))

        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE, 4 * 6, ctypes.c_void_p(4*3))

        glEnableVertexAttribArray(1)

        glDrawArrays(GL_TRIANGLES, 0 , int(len(self.vertBuffer) / 6))




class Renderer:
    """openGL renderer with opengl and pygame"""
    def __init__(self, screen) -> None:

        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()
        

        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.width, self.height)

        self.scene = []
        self.active_shader = None

        #viewmatrix
        self.camPosition = glm.vec3(0,0,0)
        self.camRotation = glm.vec3(0,0,0)
        self.viewMatrix = self.getViewMatrix()

        #projection matrix
        self.projectionMatrix = glm.perspective(glm.radians)


    
    
    def setShaders(self, vertexShader, fragmentShader):
        if vertexShader is not None and fragmentShader is not None:
            self.active_shader = compileProgram(compileShader(vertex_shader, GL_VERTEX_SHADER), compileShader(fragment_shader, GL_FRAGMENT_SHADER))
        else:
            self.active_shader = None



    def update(self):
        self.viewMatrix = self.getViewMatrix()


    def getModelMatrix(self):
        identity = glm.mat4(1)

        translateMat = glm.translate(identity, self.position)
        pitch = glm.rotate(1,0,0)
        pitch = glm.rotate(0,1,0)
        pitch = glm.rotate(0,0,1)
        pitch = glm.rotate(xd)


    def render(self):
                   #  r   g   b   alpha
        glClearColor(0.2,0.2,0.2, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.active_shader is not None:
            glUseProgram(self.active_shader)

            glUniformMatrix4fv( glGetUniformLocation(self.active_shader, "viewMatrix"), 1, GL_FALSE, glm.value_ptr(self.viewMatrix()) )

            glUniformMatrix4fv( glGetUniformLocation(self.active_shader, "projectionMatrix"), 1, GL_FALSE, glm.value_ptr(self.viewMatrix()) )


        for obj in self.scene:
            if aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            obj.render()
