import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("black")
    brad.speed(4)
    for i in range(1,36):
          draw_square(brad)
          brad.right(10)

draw_art()
window.exitonclick()
draw_square()
