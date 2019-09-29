import turtle
import math

# set radius and theta
radius = 200
theta=1
# calculate rates
lr_rate = 3/math.sqrt(3)
new_r_rate = 0.5/math.sin(math.radians(150-theta))
length = radius * lr_rate

# Draw the first triangle
def tri_1():
    trian.penup()
    trian.left(90)
    trian.forward(radius)
    trian.left(150)
    trian.pendown()

    trian.forward(length)
    for i in range(2):
        trian.left(120)
        trian.forward(length)

# Draw the inner triangle
def triangle(radius, length):
    for i in range(30):
        c = ['red','orange','yellow','green','blue']
        for i in c:
            trian.color(i)
            trian.right(30)
            trian.penup()
            trian.backward(radius)
            trian.left(theta)
            radius=radius*new_r_rate
            length=radius*lr_rate
            trian.forward(radius)
            trian.left(150)
            trian.pendown()
            trian.forward(length)
            for i in range(2):
                trian.left(120)
                trian.forward(length)




if __name__=='__main__':
    trian = turtle.Turtle()
    trian.speed(0)
    trian.color("red")
    tri_1()
    triangle(radius,length)
    turtle.done()


# for i in range(20):
#     triangle("red",2)
#     triangle("orange",2)
    # triangle("yellow",radius,length)
    # triangle("green",radius,length)
    # triangle("blue",radius,length)
    # triangle("darkblue",radius,length)
    # triangle("purple",radius,length)

