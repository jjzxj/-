import turtle as t

t.hideturtle()

def start(x,y,right,f):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.right(right)
    t.color('yellow','yellow')
    t.begin_fill()
    for i in range (5):
        t.forward(f)
        t.right(144)
    t.end_fill()
def rectangle(x,y,c,k):
    t.penup()
    t.goto(-575,383)
    t.pendown()
    t.color('red','red')
    t.begin_fill()
    for i in range(1):
        t.forward(c)
        t.right(90)
        t.forward(k)
        t.right(90)
        t.forward(c)
        t.right(90)
        t.forward(k)
    t.end_fill()
rectangle(-575,383,1151,767)
start(-384,307.2,162,228)
start(-230.4,290,240,76)
start(-150,220,20,76)
start(-150,120,25,76)
start(-230,70,25,76)
