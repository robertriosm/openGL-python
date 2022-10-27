import pygame
import pygame.time
import pygame.event
import pygame.key
from pygame.locals import *
import pygame.display
import gl
from gl import Buffer

width = 256
height = 256

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

            #position      #color
triangle = [1,1,1,          1,0,0,
            0.7,0.4,1.6,    0,1,0,
            -1.2,2,-2.6,    0,0,1 ]

triangle = Buffer(triangle)
triangle =


rend = gl.Renderer(screen=screen)

rend.scene.append(gl.Buffer(triangle))

isRunning = True

while isRunning:

    # keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False


    deltaTime = clock.tick(60) / 1000
    # print(deltaTime) cada segundo imprime 0.016 ~ 0.017

    rend.render()

    pygame.display.flip()

pygame.quit()

