import turtle

smiles = turtle.Turtle()
turtle.penup()
turtle.goto(-75,150)
turtle.pendown()
turtle.circle(10)     

turtle.penup()
turtle.goto(75,150)
turtle.pendown()
turtle.circle(10)     

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.circle(100,90)   

turtle.penup()
turtle.setheading(180)
turtle.goto(0,0)
turtle.pendown()
turtle.circle(-100,90)

s = turtle.getscreen()