import turtle
import random

screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)  

WINNING_SCORE = 5
BALL_SPEED = 10  

left_player = 0
right_player = 0
game_state = "start"  

def create_ball():
    b = turtle.Turtle()
    b.speed(0)
    b.shape("circle")
    b.color("orange")
    b.penup()
    b.goto(0, 0)
    b.dx = BALL_SPEED
    b.dy = -BALL_SPEED
    b.hideturtle()
    return b


def create_paddle(x, y):
    p = turtle.Turtle()
    p.speed(0)
    p.shape("square")
    p.color("white")
    p.shapesize(stretch_wid=6, stretch_len=2)
    p.penup()
    p.goto(x, y)
    return p


left_pad = create_paddle(-400, 0)
right_pad = create_paddle(400, 0)
ball = create_ball()

score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.color("white")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 260)

message_writer = turtle.Turtle()
message_writer.speed(0)
message_writer.color("yellow")
message_writer.penup()
message_writer.hideturtle()

def move_up(pad):
    y = pad.ycor()
    if y < 250:
        pad.sety(y + 100)


def move_down(pad):
    y = pad.ycor()
    if y > -240:
        pad.sety(y - 100)

screen.listen()
screen.onkeypress(lambda: move_up(left_pad), "w")
screen.onkeypress(lambda: move_down(left_pad), "s")
screen.onkeypress(lambda: move_up(right_pad), "Up")
screen.onkeypress(lambda: move_down(right_pad), "Down")

def update_score():
    score_writer.clear()
    score_writer.write(
        f"LeftPlayer: {left_player}    RightPlayer: {right_player}",
        align="center",
        font=("Courier", 24, "bold"),
    )

def show_message(title, subtitle=""):
    message_writer.clear()
    message_writer.goto(0, 10)
    message_writer.write(title, align="center", font=("Courier", 36, "bold"))
    if subtitle:
        message_writer.goto(0, -40)
        message_writer.write(subtitle, align="center", font=("Courier", 18, "normal"))

def clear_message():
    message_writer.clear()

def reset_ball(direction):
    ball.goto(0, 0)
    ball.dx = BALL_SPEED * direction
    ball.dy = BALL_SPEED * random.choice([-1, 1])

def start_game():
    global game_state
    clear_message()
    ball.showturtle()
    reset_ball(random.choice([-1, 1]))
    game_state = "playing"
    game_loop()

def resume_game():
    global game_state
    clear_message()
    ball.showturtle()
    reset_ball(random.choice([-1, 1]))
    game_state = "playing"
    game_loop()

def restart_game():
    global game_state, left_player, right_player
    left_player = 0
    right_player = 0
    update_score()
    left_pad.goto(-400, 0)
    right_pad.goto(400, 0)
    clear_message()
    ball.showturtle()
    reset_ball(random.choice([-1, 1]))
    game_state = "playing"
    game_loop()

def on_click(x, y):
    if game_state == "start":
        start_game()
    elif game_state == "point_scored":
        resume_game()
    elif game_state == "game_over":
        restart_game()

screen.onclick(on_click)

def game_loop():
    global game_state, left_player, right_player

    if game_state != "playing":
        return

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top / bottom wall bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # paddle collisions
    if (ball.xcor() > 380 and ball.dx > 0 and
            right_pad.ycor() - 60 < ball.ycor() < right_pad.ycor() + 60):
        ball.setx(380)
        ball.dx *= -1

    if (ball.xcor() < -380 and ball.dx < 0 and
            left_pad.ycor() - 60 < ball.ycor() < left_pad.ycor() + 60):
        ball.setx(-380)
        ball.dx *= -1

    # scoring
    scored_side = None
    if ball.xcor() > 490:
        left_player += 1
        scored_side = "Left"
    elif ball.xcor() < -490:
        right_player += 1
        scored_side = "Right"

    if scored_side:
        update_score()
        ball.hideturtle()
        ball.goto(0, 0)

        if left_player >= WINNING_SCORE or right_player >= WINNING_SCORE:
            game_state = "game_over"
            winner = "Left Player" if left_player > right_player else "Right Player"
            show_message(f"{winner} Wins!", "Click anywhere to Restart")
        else:
            game_state = "point_scored"
            show_message(f"{scored_side} Player Scores!", "Click anywhere to Continue")

        screen.update()
        return  

    screen.update()
    screen.ontimer(game_loop, 8) 

def main():
    update_score()
    show_message("PONG", "Click anywhere to Start")
    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    main()