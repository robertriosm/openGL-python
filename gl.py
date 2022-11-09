
import glm
from numpy import array, float32
from OpenGL.GL import *
from ctypes import c_void_p
from OpenGL.GL.shaders import compileProgram, compileShader
from shaders import * 
from obj import Obj
from pygame import image


class Model(object):
    def __init__(self, objName, textureName):
        self.model = Obj(objName)

        self.createVertexBuffer()
        
        self.position = glm.vec3(0,0,0)
        self.rotation = glm.vec3(0,0,0)
        self.scale = glm.vec3(1,1,1)

        self.textureSurface = image.load(textureName)
        self.textureData = image.tostring(self.textureSurface, "RGB", True)

        self.texture = glGenTextures(1)


    def createVertexBuffer(self):
        buffer = []

        self.polycount = 0

        for face in self.model.faces:
            self.polycount += 1

            for i in range(3):
                # positions
                pos = self.model.vertices[face[i][0] - 1]
                buffer.append(pos[0])
                buffer.append(pos[1])
                buffer.append(pos[2])

                # texcoords
                uvs = self.model.texcoords[face[i][1] - 1]
                buffer.append(uvs[0])
                buffer.append(uvs[1])

                # normals
                norm = self.model.normals[face[i][2] - 1]
                buffer.append(norm[0])
                buffer.append(norm[1])
                buffer.append(norm[2])

            if len(face) == 4:

                self.polycount += 1

                for i in [0,2,3]:
                    # positions
                    pos = self.model.vertices[face[i][0] - 1]
                    buffer.append(pos[0])
                    buffer.append(pos[1])
                    buffer.append(pos[2])

                    # texcoords
                    uvs = self.model.texcoords[face[i][1] - 1]
                    buffer.append(uvs[0])
                    buffer.append(uvs[1])

                    # normals
                    norm = self.model.normals[face[i][2] - 1]
                    buffer.append(norm[0])
                    buffer.append(norm[1])
                    buffer.append(norm[2])


        self.vertBuffer = array(buffer, dtype = float32)
        
        # Vertex Buffer Object
        self.VBO = glGenBuffers(1)
        # Vertex Array Object
        self.VAO = glGenVertexArrays(1)

    def getModelMatrix(self):
        identity = glm.mat4(1)

        translateMat = glm.translate(identity, self.position)

        pitch = glm.rotate(identity, glm.radians(self.rotation.x), glm.vec3(1,0,0))
        yaw   = glm.rotate(identity, glm.radians(self.rotation.y), glm.vec3(0,1,0))
        roll  = glm.rotate(identity, glm.radians(self.rotation.z), glm.vec3(0,0,1))

        rotationMat = pitch * yaw * roll

        scaleMat = glm.scale(identity, self.scale)

        return translateMat * rotationMat * scaleMat

    def render(self):

        glBindBuffer(GL_ARRAY_BUFFER, self.VBO)
        glBindVertexArray(self.VAO)

        # Mandar la informacion de vertices
        glBufferData(GL_ARRAY_BUFFER,           # Buffer ID
                     self.vertBuffer.nbytes,    # Buffer size in bytes
                     self.vertBuffer,           # Buffer data
                     GL_STATIC_DRAW)            # Usage

        # Atributos

        # Atributo de posiciones
        glVertexAttribPointer(0,                # Attribute number
                              3,                # Size
                              GL_FLOAT,         # Type
                              GL_FALSE,         # Is it normalized
                              4 * 8,            # Stride
                              ctypes.c_void_p(0))# Offset

        glEnableVertexAttribArray(0)

        # Atributo de texcoords
        glVertexAttribPointer(1,                # Attribute number
                              2,                # Size
                              GL_FLOAT,         # Type
                              GL_FALSE,         # Is it normalized
                              4 * 8,            # Stride
                              ctypes.c_void_p(4*3))# Offset

        glEnableVertexAttribArray(1)

        # Atributo de normals
        glVertexAttribPointer(2,                # Attribute number
                              3,                # Size
                              GL_FLOAT,         # Type
                              GL_FALSE,         # Is it normalized
                              4 * 8,            # Stride
                              ctypes.c_void_p(4*5))# Offset

        glEnableVertexAttribArray(2)


        # Dar la textura
        glActiveTexture( GL_TEXTURE0 )
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexImage2D(GL_TEXTURE_2D,                     # Texture Type
                     0,                                 # Positions
                     GL_RGB,                            # Format
                     self.textureSurface.get_width(),   # Width
                     self.textureSurface.get_height(),  # Height
                     0,                                 # Border
                     GL_RGB,                            # Format
                     GL_UNSIGNED_BYTE,                  # Type
                     self.textureData)                  # Data

        glGenerateMipmap(GL_TEXTURE_2D)



        glDrawArrays(GL_TRIANGLES, 0, self.polycount * 3 )


class Buffer:
    """buffer class to generate objects"""
    def __init__(self, data) -> None:
        self.data = data
        self.createVertexBuffer()

        self.createVertexBuffer()

        self.position = glm.vec3(0,0,0)

        self.rotation = glm.vec3(0,0,0)

        # self.


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

        self.filledMode()

        self.scene = []
        self.active_shader = None

        self.pointLight = glm.vec3(0,0,0)
        self.value = 0
        self.time = 0

        self.deltaTime = 0

        self.target = glm.vec3(0,0,0)
        self.angle = 0
        self.camDistance = 5

        #viewmatrix
        self.camPosition = glm.vec3(0,0,0)
        self.camRotation = glm.vec3(0,0,0)
        self.viewMatrix = self.getViewMatrix()

        #projection matrix
        self.projectionMatrix = glm.perspective(glm.radians(60),        # FOV
                                                self.width/self.height, # Aspect Ratio
                                                0.1,                    # Near Plane
                                                1000) 


    def filledMode(self):
        glPolygonMode(GL_FRONT, GL_FILL)


    def wireframeMode(self):
        glPolygonMode(GL_FRONT, GL_LINE)
    
    def shader1(self):
        pass

    def shader1(self):
        pass


    def getViewMatrix(self):
        identity = glm.mat4(1)

        translateMat = glm.translate(identity, self.camPosition)

        pitch = glm.rotate(identity, glm.radians(self.camRotation.x), glm.vec3(1,0,0))
        yaw   = glm.rotate(identity, glm.radians(self.camRotation.y), glm.vec3(0,1,0))
        roll  = glm.rotate(identity, glm.radians(self.camRotation.z), glm.vec3(0,0,1))

        rotationMat = pitch * yaw * roll

        camMatrix = translateMat * rotationMat

        return glm.inverse(camMatrix)
    


    def setShaders(self, vertexShader, fragmentShader):
        if vertexShader is not None and fragmentShader is not None:
            self.active_shader = compileProgram(compileShader(vertex_shader, GL_VERTEX_SHADER), compileShader(fragment_shader, GL_FRAGMENT_SHADER))
        else:
            self.active_shader = None



    def update(self):
        # self.viewMatrix = self.getViewMatrix()
        self.viewMatrix = glm.lookAt(self.camPosition, self.target, glm.vec3(0,0.1,0.0))



    def render(self):
        glClearColor(0.2,0.2,0.2, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.active_shader is not None:
            glUseProgram(self.active_shader)

            glUniformMatrix4fv( glGetUniformLocation(self.active_shader, "viewMatrix"),
                                1, GL_FALSE, glm.value_ptr(self.viewMatrix))

            glUniformMatrix4fv( glGetUniformLocation(self.active_shader, "projectionMatrix"),
                                1, GL_FALSE, glm.value_ptr(self.projectionMatrix))

            glUniform1i(glGetUniformLocation(self.active_shader, "tex"), 0)

            glUniform1f( glGetUniformLocation(self.active_shader, "time"), self.time)   

            glUniform3fv(glGetUniformLocation(self.active_shader, "pointLight"), 1, glm.value_ptr(self.pointLight))

        for obj in self.scene:
            if self.active_shader is not None:
                glUniformMatrix4fv( glGetUniformLocation(self.active_shader, "modelMatrix"),
                                    1, GL_FALSE, glm.value_ptr(obj.getModelMatrix()))


            obj.render()

