
# Making a compass

#September 22, 2019

#CTI-110 P2HW2 - Turtle Graphic

#Doreen Strickland

#Doing a compass drawomg using python turtle

import turtle
turtle.penup()
turtle.goto(0,-20)
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,60)
turtle.write(' North')
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(60,0)
turtle.write(' East')
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,-60)
turtle.write(' South')
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-60,0)
turtle.penup()
turtle.goto(-90,0)
turtle.write(' West')
turtle.hideturtle()
