import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#CDBF1D")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
'''
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(180)
turtle_instance_2.forward(100)
'''

# square
'''
for i in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)
'''

# star
'''
for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(200)
'''

# polygon
num_sides = 5
angle = 360.0 / num_sides
side_length = 100
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()
