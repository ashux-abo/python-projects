import turtle


t = turtle.Turtle();
turtle.colormode(255) 

set_pink = (244, 165, 170)
set_red = (224, 0, 91)
set_blue = (1, 116, 194)
set_blush = (235, 103, 150)

def kirby_body():
    t.color('black', set_pink)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def draw_oblong(x, y, long_r, short_r):
    t.penup()
    t.goto(x, y)
    t.setheading(50)
    t.color('black', set_blue)
    t.pendown()
    for _ in range(2):
        t.begin_fill()
        t.circle(long_r, 90)
        t.circle(short_r, 90)
        t.end_fill()

def draw_shape(x, y, long_r, short_r, heading, flip=False, set_color=""):
    t.penup()
    direction = -1 if flip else 1
    t.goto(x, y)
    t.setheading(heading)
    t.pencolor(set_color)
    t.fillcolor(set_color)
    for _ in range(2):
        t.pendown()
        t.begin_fill()
        t.circle(long_r * direction, 90)
        t.circle(short_r * direction, 90)
        t.end_fill()
        t.penup()

def kirby_eyes(long_r, short_r):
    draw_oblong(-20, 100, long_r, short_r)
    draw_oblong(30, 100,  long_r, short_r)

def draw_pupils(x, y, long_r, short_r, heading, set_color=""):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pensize(2)
    t.pencolor(set_color)
    t.fillcolor(set_color)
    for _ in range(2):
        t.pendown()
        t.begin_fill()
        t.circle(long_r, 90)
        t.circle(short_r, 90)
        t.end_fill()


def draw_smile(x, y):
    t.penup()
    t.goto(x, y)
    t.color('black')
    t.setheading(-60)
    t.pendown()
    t.pensize(4)
    t.circle(20, 130)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    kirby_body()
    kirby_eyes(30, 10)
    draw_smile(-20, 90)

    #hand
    draw_shape(-80, 90, 30, 20, 90, flip=False, set_color=set_pink)
    draw_shape(80, 90, 30, 20, 90, flip=True, set_color=set_pink)

    #foot
    draw_shape(-30, 10, 40, 30, 90, flip=False, set_color=set_red)
    draw_shape(30, 10, 40, 30, 90, flip=True, set_color=set_red)

    draw_pupils(-22, 112, 18, 12, 50,set_color="black")
    draw_pupils(30, 112, 18, 12, 50, set_color="black")

    draw_pupils(-26, 126, 12, 5, 50,set_color="white")
    draw_pupils(26, 126, 12, 5, 50, set_color="white")

    #blush
    draw_shape(-40, 90, 10, 18, 90, flip=False, set_color=set_blush)
    draw_shape(40, 90, 10, 18, 90, flip=True, set_color=set_blush)
    
    turtle.done()

if __name__ == "__main__":
    main()

