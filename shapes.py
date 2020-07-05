# This is a custom module that has been created
# It allows us to draw shapes

import turtle

def creating_turtle():
	marco = turtle.Turtle()
	marco.shape("turtle")
	marco.speed(5)

def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()

def draw_triangle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (3):
    turtle.forward(size*3)
    turtle.left(120)
  turtle.end_fill()
  turtle.setheading(0)

def draw_square(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (4):
    turtle.forward(size*2)
    turtle.left(90)
  turtle.end_fill()
  turtle.setheading(0)

def draw_star(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.right(144)
  for i in range(5):
    turtle.forward(size*2)
    turtle.right(144)
    turtle.forward(size*2)
  turtle.end_fill()
  turtle.setheading(0)
