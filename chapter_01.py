import turtle

# guess what's returned from the following code?
print(print(1))

# guess what's returned from the following code?
print(print(1 + 2))

# round real numbers to the nearest even number
print(round(1.5)) # 2
print(round(2.5)) # 2
print(round(3.5)) # 4
print(round(4.5)) # 4
print(round(5.5)) # 6
print(round(6.5)) # 6


# GUI Programming
# turtle draw square 100x100
turtle.showturtle()
turtle.write("Welcome to Turtle Graphics!")
turtle.shape("turtle")  # change the turtle shape
turtle.delay(200)  # change the turtle speed

#draw 100 down
turtle.right(90)
turtle.forward(100)
#draw 100 left
turtle.right(90)
turtle.forward(100)
#draw 100 up
turtle.right(90)
turtle.forward(100)
#draw 100 right
turtle.right(90)
turtle.forward(100)

