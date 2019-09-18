import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    draw_square()
    draw_circle()
    draw_triangle()
    
    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(6)
    i = 0
    while(i < 4):
        brad = turtle.forward(100)
        brad = turtle.right(90)
        i = i+1
    
def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)
    
def draw_triangle():
    hui = turtle.Turtle()
    hui.shape("circle")
    hui.color("white")
    t = 0
    while(t<3):
        hui.forward(100)
        hui.left(120)
        t=t+1
    

draw_shapes()
