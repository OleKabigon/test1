#Simple Python Game using Classes

import turtle
import math
import random
import os

#Set up screen
wn = turtle.Screen() #create screen object
wn.bgcolor("red")
wn.title("Simple turtle game")

class Border(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("yellow")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-250, -250)
        self.pendown()
        self.goto(-250, 250)
        self.goto(250, 250)
        self.goto(250, -250)
        self.goto(-250, -250)



class Player(turtle.Turtle):  #initial player class, parent is turtle.Turtle

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("turtle")
        self.color("blue")
        self.speed = 1



#Class methods
    def move(self):
        self.forward(self.speed)

        #Check for Border
        if self.xcor()>238 or self.xcor() < -238:
            self.left(45)
        if self.ycor()>238 or self.ycor() < -238:
            self.left(45)


    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed += 1

    def decrespeed(self):
        self.speed -= 1

class Goal(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("circle")
        self.speed = (random.randint(1, 5))
        self.goto(random.randint(-230, 230), random.randint(-230, 230))
        self.setheading(random.randint(0, 360))

    def jump(self):
        self.goto(random.randint(-230, 230), random.randint(-230, 230))
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(self.speed)

        #Check for Border
        if self.xcor()>238 or self.xcor() < -238:
            self.left(60)
            self.speed = (random.randint(1, 5))
        if self.ycor()>238 or self.ycor() < -238:
            self.left(60)
            self.speed = (random.randint(1, 5))

# Collision checking function using pythagorean theorem to measure dist
def isCollision(t1, t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    dist = math.sqrt((a ** 2) + (b ** 2))

    if dist < 20:
        return True
    else:
        return False


player = Player() #player instance, member of player class ClassName(object):
border = Border()
goal = Goal()


#Draw the Border
border.draw_border()

#Set keyboard bindings, part of turtle
turtle.listen()
turtle.onkey(player.turnleft, "a")
turtle.onkey(player.turnright, "d")
turtle.onkey(player.increasespeed, "w")
turtle.onkey(player.decrespeed, "s")
#Main loop, this is where the action happens
while True:
    player.move()
    goal.move()

# Check for collision
    if isCollision(player, goal):
        goal.jump()
