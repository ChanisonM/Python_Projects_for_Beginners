import turtle

sceen = turtle.Screen()
sceen.title("Tic Tac Toe")

length = 300
thick = 2
color = "red"

t = turtle.Turtle()
t.color(color)
t.width(thick)
t.speed(2)



# Loop for making outside square of
# length 300
for i in range(4):
    t.forward(length)
    t.left(90)

# code for inner lines of the square
t.penup()
t.goto(0,100)
t.pendown()

t.forward(length)

t.penup()
t.goto(0,200)
t.pendown()

t.forward(length)

t.penup()
t.goto(100,0)
t.pendown()

t.left(90)
t.forward(length)
 
t.penup()
t.goto(200,0)
t.pendown()

t.forward(length)


turtle.done()