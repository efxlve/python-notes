import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("white")
turtle.speed(0)

turtle_colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.mainloop()
#turtle.done()
