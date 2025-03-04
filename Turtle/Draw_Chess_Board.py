import turtle

screen = turtle.Screen()
screen.title("Draw_Chess_Board")
pen = turtle.Turtle()

def draw():
    for i in range(4):
        pen.forward(30)
        pen.left(90)
    pen.forward(30)

if __name__ == "__main__" :
     # set screen 
    screen.setup(600 , 600)
    # set turtle object speed 
    pen.speed(100)

     # loops for board
    for i in range(8):
        pen.up()
        pen.setpos(0 , 30 * i)
        pen.down()

        # row
        for j in range(8):
            if (i + j) % 2 == 0 :
                col = "black"
            else :
                col = "white"
            pen.fillcolor(col)
            pen.begin_fill()
            draw()
            pen.end_fill()
        pen.hideturtle()

turtle.done()
