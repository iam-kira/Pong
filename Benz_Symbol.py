import turtle as t
import random

window = t.Screen()
fred = t.Turtle()

t.speed(10)
t.colormode(255)
t.bgcolor("black")
def color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color= (r,g,b)
    
    return color


# i=0
# while True:

#     for _ in range(3):
#         t.fd(i)
#         t.left(120)
#         t.pencolor(color())
#         i+=10



t.pencolor("white")

t.left(90)
for i in range(3):
    t.pencolor("grey")
    t.fd(150)
    t.bk(150)
    t.rt(120)


t.lt(60)

for i in range(3):
    t.pencolor("grey")
    t.color("grey")
    t.begin_fill()
    t.fd(22)
    t.bk(22)
    t.rt(120)
    t.end_fill()



for i in range(1):
    t.pencolor("grey")
    
    t.rt(60)
    t.fd(150)
    t.rt(172.5)
    t.fd(142)
    t.lt(45)
    t.fd(142)
    t.rt(165)
    t.fd(142)
    t.lt(45)
    t.fd(142)
    t.rt(165)
    t.fd(142)
    t.lt(45)
    t.fd(142)
    t.rt(82)
    t.circle(-150)


    # t.goto(0,170)
    # t.circle(-150)

    # t.penup()


def wait():
    i=0
    while i<150:
        print("Baka!")
        i+=1

window.onkeypress(wait(), 'space')
window.listen()
t.done()