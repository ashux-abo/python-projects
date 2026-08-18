import turtle
import random

t = turtle.Turtle();
t.speed(10)
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("02 Laboratory Exercise 1")
screen.colormode(255)

def move(heading):
    t.penup()
    t.setheading(heading)
    t.forward(100)

def movement(screen):
    screen.onkey(lambda: move(180), "Left")
    screen.onkey(lambda: move(90), 'Up')
    screen.onkey(lambda: move(0), 'Right')
    screen.onkey(lambda: move(270), 'Down')

def buttons(screen):
    screen.onkey(lambda: draw_circle(random_size()), "z")
    screen.onkey(lambda: draw_square(random_size()), "x")
    screen.onkey(lambda: draw_triangle(random_size()), "c")

def draw_circle(r_shape):
    t.fillcolor(random_color())
    t.pendown()
    t.begin_fill()
    t.circle(r_shape)
    t.end_fill()
    t.penup()

def draw_triangle(r_shape):
    t.fillcolor(random_color())
    t.pendown()
    t.begin_fill()
    for _ in range(3):
        t.forward(r_shape)
        t.left(120)
    t.end_fill()
    t.penup()

def draw_square(r_shape):
    t.fillcolor(random_color())
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(r_shape)
        t.right(90)
    t.end_fill()
    t.penup()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def random_size():
    return random.randint(20, 50)


def main():
    screen.listen()

    movement(screen=screen)
    buttons(screen=screen)

    turtle.done()


if __name__ == "__main__":
    main()