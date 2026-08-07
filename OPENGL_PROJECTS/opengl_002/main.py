import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, 1, 1), 
    (1, 1, -1), 
    (1, -1, -1), 
    (1, -1, 1), 
    (-1, 1, 1), 
    (-1, -1, -1), 
    (-1, -1, 1), 
    (-1, 1, -1)
)

edges= (
    (0, 1), 
    (0, 3), 
    (0, 4), 
    (1, 2), 
    (1, 7), 
    (2, 5), 
    (2, 3), 
    (3, 6), 
    (4, 6), 
    (4, 7), 
    (5, 6), 
    (5, 7)
)

quads = (
    (0, 3, 6, 4), 
    (2, 3, 6, 5), 
    (0, 1, 7, 4), 
    (1, 2, 5, 7), 
    (0, 1, 2, 3),
    (4, 7, 5, 6)
)

colors = (
    (0.8, 0.2, 0.2), # Red
    (0.2, 0.8, 0.2), # Green
    (0.2, 0.2, 0.8), # Blue
    (0.8, 0.8, 0.2), # Yellow
    (0.2, 0.8, 0.8), # Cyan
    (0.8, 0.2, 0.8)  # Magenta
)
def Cube():
    glBegin(GL_QUADS)
    for quad in quads:
        x = 0
        for vertex in quad:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glLineWidth(2.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    display = (800, 600)
    windows_flag = (pg.OPENGL | pg.DOUBLEBUF)
    screen_color = (0.5, 0, 0.25, 1.0)
    fps = 60

    pg.init()

    
    screen = pg.display.set_mode(display, windows_flag)
    clock = pg.time.Clock()

    # setup projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # setup modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)

    glEnable(GL_DEPTH_TEST)
    glClearColor(*screen_color)
    running = True
    while running:
        for event in pg.event.get(): 
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                running = False
                break

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(0.5, 1, 2, 0)

        Cube()

        pg.display.flip()
        clock.tick(fps) 
    pg.quit()

if __name__  == "__main__":
    main()