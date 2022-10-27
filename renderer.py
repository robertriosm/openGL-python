import pygame
import pygame.time
import pygame.event
import pygame.key
from pygame.locals import *
import pygame.display
import gl
from gl import Renderer, Model
from shaders import *

width = 256
height = 256

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen=screen)


            # position      #color
triangle = [1,1,1,          1,0,0,
            0.7,0.4,1.6,    0,1,0,
            -1.2,2,-2.6,    0,0,1 ]

# triangle = Buffer(triangle)


rend = gl.Renderer(screen=screen)

# rend.scene.append(gl.Buffer(triangle))

rend.setShaders(vertex_shader, fragment_shader)

face = Model("model.obj")

face.position.z -= 10

rend.scene.append(face)


# scene:

isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    
    if keys[K_LEFT]:
        rend.camPosition.x -= 10*deltaTime
    
    elif keys[K_RIGHT]:
        rend.camPosition.x += 10 * deltaTime
    



    deltaTime = clock.tick(60) / 1000
    # print(deltaTime) cada segundo imprime 0.016 ~ 0.017

    rend.update()

    rend.render()

    pygame.display.flip()

pygame.quit()

