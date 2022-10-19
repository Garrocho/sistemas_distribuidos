import turtle
import time
import random

delay = 0.01

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Move Game by @Garrocho")
wn.bgcolor("green")
wn.setup(width=1.0, height=1.0, startx=None, starty=None)
wn.tracer(0) # Turns off the screen updates

# gamer 1
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def close():
    wn.bye()

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 2)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 2)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 2)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 2)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(close, "Escape")

# Main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)


wn.mainloop()
