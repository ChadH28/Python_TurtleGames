import os
import random
import turtle
import time

#created delay for refresh rate
delay = 0.05

screen = turtle.Screen()
screen.title("Spaceship Wars     By: Chad Hoosain")
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.tracer(0)

#screen.bgpic("bg1.gif", width= 1000,height= 600)
screen.bgpic("bg (2).gif")

# line boundary
l = turtle.Turtle()
l.hideturtle()
l.speed(25)
l.color("white")
l.pensize(5)
l.penup()
l.left(90)
l.forward(300)
l.pendown()
l.left(90)
l.forward(500)
l.left(90)
l.forward(600)
l.left(90)
l.forward(1000)
l.left(90)
l.forward(600)
l.left(90)
l.forward(1000)

#game menus
def game():
    level = 1
    score = 0
    state = "playing"
    lives = 3
game()

#spaceship
spaceship = turtle.Turtle()
spaceship.speed(0)   # speed of module, fastest speed
#screen.register_shape("ship.gif")
spaceship.shape("triangle")
spaceship.color("yellow")
spaceship.penup()
spaceship.goto(0,0)
spaceship.speed = 3

#spaceship missile
missile = turtle.Turtle()
missile.speed(0)   # speed of module, fastest speed
#screen.register_shape("ship.gif")
missile.shape("circle")
missile.shapesize(0.5)
missile.color("lime green")
missile.penup()
missile.goto(0,0)
missile.speed = 20
missile.status = "ready"

def fire():
    if missile.status == "ready":
        missile.status == "shoot"
def missile_firing():
    if missile.status == "firing":
        missile.forward(missile.speed)

#enemy
enemy = turtle.Turtle()
enemy.speed(0)   # speed of module, fastest speed
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.setheading(random.randint(0,360))
enemy.speed = 5
enemy.dx =1
enemy.dy =1


def constant_movement():
    spaceship.forward(spaceship.speed)

def enemy_movement():
    enemy.forward(enemy.speed)

def accelerate():
        spaceship.speed += 1
def decelerate():
        spaceship.speed -= 1
def go_left():
        spaceship.left(45)
def go_right():
        spaceship.right(45)



#keybindings
screen.listen()
screen.onkeypress(accelerate, "Up")
screen.onkeypress(decelerate,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")
screen.onkeypress(fire, "space")




#main game loop
while True:
    screen.update()
    #movement of enemy
    enemy.setx(enemy.xcor() + enemy.dx)
    enemy.sety(enemy.ycor() + enemy.dy)
    enemy_movement()

    # Check for a collision with the border
    if spaceship.xcor() > 499 or spaceship.xcor() < -499 or spaceship.ycor() > 299 or spaceship.ycor() < -299:
        time.sleep(0.5)
        spaceship.goto(0,0)

    #border collisions
    if enemy.ycor() > 299:   #if ball collides with the border it will bounce back
        enemy.sety(299)
        enemy.dy *= -1 + enemy.speed #reverses direction of the BALL
        enemy.speed = 6
        #winsound.Playsound("", winsound.SND_ASYNC)

    #enemy boundaries
    if enemy.ycor() < -299:
        enemy.sety(-299)
        enemy.dy *= -1 #reverses direction of the BALL

    if enemy.xcor() > 499:
        enemy.setx(499)
        enemy.dx *= -1

    if enemy.xcor() < -499:
        enemy.setx(-499)
        enemy.dx *= -1

    # Player and enemy collsion
    if (spaceship.xcor() >= (enemy.xcor() - 20))and (spaceship.xcor() <= (enemy.xcor() + 20)) and (spaceship.ycor() <= (enemy.ycor() + 20)) and (spaceship.ycor() >= (enemy.ycor() - 20)):
        spaceship.goto(0,0)


    constant_movement()
    accelerate()
    decelerate()
    go_left()
    go_right()
    time.sleep(delay)
screen.update()
