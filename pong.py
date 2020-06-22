import turtle
import winsound

#screen setup
screen = turtle.Screen()
screen.title("Pong     By: Chad Hoosain")
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

# start circle
cir = turtle.Turtle()
cir.hideturtle()
cir.right(90)
cir.penup()
cir.forward(40)
cir.pendown()
cir.left(90)
cir.pensize(5)
cir.color('white')
cir.circle(40)


#paddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0)   #speed of paddle animation.
paddle_a.shape("square")
paddle_a.color("magenta")
paddle_a.shapesize(stretch_wid= 5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)

#paddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0)   #speed of paddle animation.
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid= 5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(360, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)   #speed of paddle animation.
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx =1
ball.dy =1

#Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("Light green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" Player A: 0  Player B: 0 ", align="center", font=("Arial", 20, "bold"))


#SCORING
score_a = 0
score_b = 0


#function for movements
def paddleA_up():
    y = paddle_a.ycor()    #this is built in turtle module to access the y coordinates of given object
    y += 20     #this moves the paddle in 20 increments
    paddle_a.sety(y)

def paddleA_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)

def paddleB_up():
    y = paddle_b.ycor()    #this is built in turtle module to access the y coordinates of given object
    y += 20     #this moves the paddle in 20 increments
    paddle_b.sety(y)

def paddleB_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)

#keybindings
screen.listen()
screen.onkeypress(paddleA_up, "a") #left paddle
screen.onkeypress(paddleA_down,"z")  #left paddle
screen.onkeypress(paddleB_up, "Up") #Right paddle
screen.onkeypress(paddleB_down,"Down")  #right paddle
#screen.onkeypress(go_left,"Left")
#screen.onkeypress(go_right,"Right")


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
        score_a += 1
        pen.clear()
        pen.write(" Player A:{} || Player B: {} ".format(score_a, score_b), align="center", font=("Arial", 20, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(" Player A: {} || Player B: {} ".format(score_a, score_b), align="center", font=("Arial", 20, "bold"))

    # Paddles and ball collsion
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    #paddle collision with border
    if paddle_b.ycor() > 300:
        paddle_b.sety(300)
    if paddle_b.ycor() < -300:
        paddle_b.sety(-300)

    if paddle_a.ycor() > 300:
        paddle_a.sety(300)
    if paddle_a.ycor() < -300:
        paddle_a.sety(-300)