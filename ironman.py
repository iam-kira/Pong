# Using pyhton turtle library
~Vijay Biradar

import turtle
import time
# V

piece1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10), (-40, -20), (0, -20)],[(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260), (40, 120), (0, 120)]]

piece2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210), (-80, -230), (-64, -210), (0, -210)],[(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]

piece3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280), (-60, -260), (-30, -260), (-20, -250), (0, -250)],[(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240), (60, -220), (0, -220)]]

piece4=[[(-40, -20),(-140, 10),(-150,-10), (-170,10), (-176, 0),  (-130, -40), (-100, -46), (-50, -40),(-40, -30)]  ,[ (0, -30),  (40, -30),(50, -40),(100,-46), (130, -40), (176, 0), (170, 10), (150, -10), (140, 10), (40,-20)]]

piece5=[[ (-110, -210), (-80, -230), (-64, -210), (0, -210), (64, -210),(80, -230) ,(110, -210), (110, -220),  (80, -240), (60, -220), (0, -220),(-60, -220), (-80, -240), (-110, -220)],[(-110,-210) ]]


bg="red"
bgg="#fab104" 
bg1="#67c7EB" 
turtle.hideturtle()
turtle.bgcolor('#6a0c0b') 
turtle.setup(500,600)
piece1Goto=(0,120)
piece2Goto=(0,-30)
piece3Goto=(0,-220)
piece4Goto=(0,-20)
piece5Goto=(-110, -210)

turtle.speed(2)
# I

turtle.color('white')
style = ('Courier', 15, 'italic')
# turtle.write('You have been hacked :)', font=style, align='center')
turtle.hideturtle()


def draw_piece(piece,pieceGoto):
    # J
    turtle.penup()
    turtle.goto(pieceGoto)
    turtle.pendown()
    turtle.color(bgg) 
    turtle.begin_fill()
    for i in range(len(piece[0])):
        x,y=piece[0][i]
        turtle.goto(x,y)
    
    for i in range(len(piece[1])):
        x,y=piece[1][i]
        turtle.goto(x,y)
    turtle.end_fill()




draw_piece(piece1,piece1Goto)
draw_piece(piece2,piece2Goto)
draw_piece(piece3,piece3Goto)
# A

def draw_piece(piece,pieceGoto):
    # Y
    turtle.penup()
    turtle.goto(pieceGoto)
    turtle.pendown()
    turtle.color(bg1) 
    turtle.begin_fill()
    for i in range(len(piece[0])):
        x,y=piece[0][i]
        turtle.goto(x,y)
    
    for i in range(len(piece[1])):
        x,y=piece[1][i]
        turtle.goto(x,y)
    turtle.end_fill()
draw_piece(piece4,piece4Goto)
draw_piece(piece5,piece5Goto)
turtle.hideturtle()
turtle.done()

time.sleep(5)
