import turtle
import webbrowser
import time

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    some_turtle.circle(100)

def draw_circle2(some_turtle):
    some_turtle.circle(125)

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.forward(250)
        some_turtle.right(120)
        
def draw_art():

    # time.sleep(10)
    #
    # webbrowser.open("https://www.youtube.com/watch?v=BVRnLUMeAoQ&list=PLmIAixrHzxnbZqAuPGHv4Vy5SosvlfxQv")
    # time.sleep(5)

    window = turtle.Screen()
    window.bgcolor("blue")
    hui = turtle.Turtle()
    hui.shape("turtle")
    hui.color("yellow")
    hui.speed(8)
# ---------------------------------------------------------------------------------------------
    for i in range(1,37):
        draw_square(hui)
        hui.right(10)

    wells = turtle.Turtle()
    wells.shape("circle")
    wells.color("yellow")
    wells.speed(9)

    for i in range(1,37):
        draw_circle(wells)
        wells.right(10)

    love = turtle.Turtle()
    love.shape("circle")
    love.color("yellow")
    love.speed(8)

    for i in range(1,37):
        draw_triangle(love)
        love.left(10)

    huilove = turtle.Turtle()
    huilove.shape("circle")
    huilove.color("yellow")
    huilove.speed(0)

    for i in range(1,37):
        draw_circle2(huilove)
        huilove.right(10)


    window.exitonclick()

draw_art()
