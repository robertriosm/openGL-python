import pygame
import pygame.time
import pygame.event
import pygame.key
from pygame.locals import *
import pygame.display
import gl
from gl import Renderer, Model
from shaders import *
from math import cos, sin, radians

width = 960
height = 540

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

face = Model("Stone.obj", "marmol.bmp")

face.position.z -= 10
face.scale.x = 0.8
face.scale.y = 0.8
face.scale.z = 0.8

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
            
            elif event.key == pygame.K_1:
                rend.filledMode()

            elif event.key == pygame.K_2:
                rend.wireframeMode()
    

    # move camera
    if keys[K_a]:
        if rend.camPosition.x > -8:
            rend.camPosition.x -= 5 * deltaTime
    
    elif keys[K_d]:
        if rend.camPosition.x < 8:
            rend.camPosition.x += 5 * deltaTime
    
    # limits
    elif keys[K_s]:
        if rend.camPosition.y > 0:
            rend.camPosition.y -= 5 * deltaTime
    
    elif keys[K_w]:
        if rend.camPosition.y < 8:
            rend.camPosition.y += 5 * deltaTime


    # zoom in and zoom out
    if keys[K_q]:
        if rend.camDistance > 2:
            rend.camDistance -= 5 * deltaTime
    
    elif keys[K_e]:
        if rend.camDistance < 8:
            rend.camDistance += 5 * deltaTime


    # lights
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime

    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime
    
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime


    # camera changes
    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance

    deltaTime = clock.tick(60) / 1000
    # print(deltaTime) cada segundo imprime 0.016 ~ 0.017

    rend.update()
    rend.render()

    pygame.display.flip()

pygame.quit()

