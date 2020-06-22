import turtle
import winsound

#screen setup
screen = turtle.Screen()
screen.title("Hockey     By: Chad Hoosain")
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.tracer(0)

# line boundary
l = turtle.Turtle()
l.hideturtle()
l.speed(25)
l.color("white")
l.pensize(5)
l.left(90)
l.forward(300)
l.left(90)
l.forward(400)
l.left(90)
l.forward(600)
l.left(90)
l.forward(800)
l.left(90)
l.forward(600)
l.left(90)
l.forward(400)
l.left(90)
l.forward(600)


#HockeyP1
HockeyP1 = turtle.Turtle()
HockeyP1.speed(0)   #speed of paddle animation.
HockeyP1.shape("circle")
HockeyP1.shapesize(40)
HockeyP1.color("magenta")
HockeyP1.shapesize(stretch_wid= 5,stretch_len=1)
HockeyP1.penup()
HockeyP1.goto(-360, 0)

#HockeyP2
HockeyP2 = turtle.Turtle()
HockeyP2.speed(0)   #speed of paddle animation.
HockeyP2.shape("circle")
HockeyP2.shapesize(40)
HockeyP2.color("cyan")
HockeyP2.shapesize(stretch_wid= 5,stretch_len=1)
HockeyP2.penup()
HockeyP2.goto(360, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)   #speed of paddle animation.
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx =1
ball.dy =1

#function for movements
def HockeyP1_up():
    y = HockeyP1.ycor()    #this is built in turtle module to access the y coordinates of given object
    y += 20     #this moves the paddle in 20 increments
    HockeyP1.sety(y)

def HockeyP1_down():
    y = HockeyP1.ycor()
    y += -20
    HockeyP1.sety(y)

def HockeyP1_left():
    x = HockeyP1.xcor()    #this is built in turtle module to access the y coordinates of given object
    x += -10     #this moves the paddle in 20 increments
    HockeyP1.setx(x)

def HockeyP1_right():
    x = HockeyP1.ycor()
    x += 5
    HockeyP1.setx(x)


def HockeyP2_up():
    y = HockeyP2.ycor()    #this is built in turtle module to access the y coordinates of given object
    y += 20     #this moves the paddle in 20 increments
    HockeyP2.sety(y)

def HockeyP2_down():
    y = HockeyP2.ycor()
    y += -20
    HockeyP2.sety(y)

def HockeyP2_left():
    x = HockeyP2.xcor()    #this is built in turtle module to access the y coordinates of given object
    x += -10     #this moves the paddle in 20 increments
    HockeyP2.setx(x)

def HockeyP2_right():
    x = HockeyP2.ycor()
    x += 10
    HockeyP2.setx(x)

#keybindings
screen.listen()
screen.onkeypress(HockeyP1_up, "Up") #left paddle
screen.onkeypress(HockeyP1_down,"Down")  #left paddle
screen.onkeypress(HockeyP1_left, "Left") #Right paddle
screen.onkeypress(HockeyP1_right,"Right")  #right paddle

screen.onkeypress(HockeyP2_up, "w") #left paddle
screen.onkeypress(HockeyP2_down,"s")  #left paddle
screen.onkeypress(HockeyP2_left, "a") #Right paddle
screen.onkeypress(HockeyP2_right,"d")  #right paddle

#main game loop
while True:
    screen.update()     #Every time it goes through the loop it updates.

    #movement of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border collisions
    if ball.ycor() > 290:   #if ball collides with the border it will bounce back
        ball.sety(290)
        ball.dy *= -1 #reverses direction of the BALL
        #winsound.Playsound("", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #reverses direction of the BALL


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        HockeyP1.goto(-360, 0)


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        HockeyP1.goto(-360, 0)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < HockeyP1.ycor() + 40 and ball.ycor() > HockeyP1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    #paddle collision with border
    if HockeyP1.ycor() > 300:
        HockeyP1.sety(300)
    if HockeyP1.ycor() < -300:
        HockeyP1.sety(-300)
