import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


                #0, 1, 2, 3, 4, 5, 6, 7
cubeVertices =((1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1), (-1, -1, 1), (-1, 1, -1))
cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7))
                # top, left, right, bottom, front, back
cubeQuads = ((0, 3, 6, 4), (2, 3, 6, 5), (0, 1, 4, 7), (1, 2, 5, 7), (0, 1, 2, 3),(6, 5, 7, 4))

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

def main():
    SCREEN_SIZE = (1380, 720)
    SCREEN_COLOR = (0.5, 0, 0.25, 1.0)
    WINDOW_CREATION_FLAGS = pg.OPENGL | pg.DOUBLEBUF
    FRAMERATE = 60

    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE, WINDOW_CREATION_FLAGS)
    clock = pg.time.Clock()

    glClearColor(*SCREEN_COLOR)

    gluPerspective(100, (SCREEN_SIZE[0]/SCREEN_SIZE[1]), 1, 50.0)

    cube_x = 0
    cube_y = 0
    player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2);
    dt = 0
    angle = 0
    glEnable(GL_DEPTH_TEST)
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False
                break
                pg.quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glTranslatef(cube_x, cube_y, -5)
        glRotatef(angle, 1, 1, 0)
        #solidCube()
        wireCube()
        glPopMatrix()

        angle += 1

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            cube_y += 3 * dt
        if keys[pg.K_s]:
            cube_y -= 3 * dt
        if keys[pg.K_a]:
            cube_x -= 3 * dt    
        if keys[pg.K_d]:
            cube_x += 3 * dt

        pg.display.flip()
        dt = clock.tick(FRAMERATE) / 1000

if __name__ == "__main__":
    main()
