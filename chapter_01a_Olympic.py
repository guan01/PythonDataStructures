import turtle
turtle.delay(10)
turtle.pensize(10)

#draw the first red circle at 0,0 radius 50
turtle.color("blue")
turtle.circle(50)

#draw the second blue circle
turtle.color("brown")
turtle.penup()
turtle.goto(125, 0)
turtle.pendown()
turtle.circle(50)

#draw the third blue circle
turtle.color("yellow")
turtle.penup()
turtle.goto(250, 0)
turtle.pendown()
turtle.circle(50)

#draw the third blue circle
turtle.color("green")
turtle.penup()
turtle.goto(62.5, -50)
turtle.pendown()
turtle.circle(50)

#draw the third black circle
turtle.color("black")
turtle.penup()
turtle.goto(187.5, -50)
turtle.pendown()
turtle.circle(50)

turtle.done()
