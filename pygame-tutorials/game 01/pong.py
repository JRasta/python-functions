"""Title: Pong
Author: J. Smith
Date: 23/11/2022
Description: A simple version of pong using pygame-tutorials
"""

import turtle

# create a turtle window
win = turtle.Screen()
win.title('Pong')
win.bgcolor('black')
win.setup(width=800, height=600)  # setup screen size
win.tracer(0)  # stops the window from updating - speeds up game - very good

# paddle_left
paddle_left = turtle.Turtle()
paddle_left.speed(0)  # sets the speed to maximum speed
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()  # turtle draws stuff, this disables this
paddle_left.goto(x=-350, y=0)

# paddle_right
paddle_right = turtle.Turtle()
paddle_right.speed(0)  # sets the speed to maximum speed
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()  # turtle draws stuff, this disables this
paddle_right.goto(x=350, y=0)

# ball
ball = turtle.Turtle()
ball.speed(0)  # sets the speed to maximum speed
ball.shape('square')
ball.color('white')
ball.penup()  # turtle draws stuff, this disables this
ball.goto(x=0, y=0)
ball.dx = 0.2
ball.dy = 0.2

# function
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


# function
def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


# open listener for the key presses
win.listen()
# left paddle
win.onkeypress(paddle_left_up, 'w')
win.onkeypress(paddle_left_down, 's')

# right paddle
win.onkeypress(paddle_right_up, 'Up')
win.onkeypress(paddle_right_down, 'Down')

# main game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:  # top border
        ball.sety(290)
        ball.dy *= -1  # reverse the direction

    if ball.ycor() < -290:  # bottom border
        ball.sety(-290)
        ball.dy *= -1  # reverse the direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # reverse the direction

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  # reverse the direction
