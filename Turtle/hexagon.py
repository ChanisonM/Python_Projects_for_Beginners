import turtle

polygon = turtle.Turtle()
num_sides = 6
side_leght = 70 
angle = 360.0/num_sides
for i in range (num_sides) :
    polygon.forward(side_leght)
    polygon.right(angle)

turtle.done()