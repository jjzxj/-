import turtle as t

t.hideturtle()

t.penup()

t.goto(-576,384)

t.pendown()

t.color('red','red')

t.begin_fill()
for i in range(1):
    t.forward(1152)
    t.right(90)
    t.forward(768)
    t.right(90)
    t.forward(1152)
    t.right(90)
    t.forward(768)
t.end_fill()

t.penup()
#第一颗星
t.goto(-384,307.2)

t.pendown()

t.right(162)
t.color('yellow','yellow')
t.begin_fill()
for i in range(5):
    t.forward(228)
    t.right(144)
t.end_fill()
#第二颗星
t.penup()

t.goto(-230.4,290)

t.pendown()

t.left(120)

t.begin_fill()
for i in range(5):
    t.forward(76)
    t.right(144)
t.end_fill()
#第三颗星
t.penup()

t.goto(-150,220)

t.pendown()

t.right(20)

t.begin_fill()
for i in range(5):
    t.forward(76)
    t.right(144)

t.end_fill()
#第四颗星
t.penup()

t.goto(-150,120)

t.pendown()

t.right(25)

t.begin_fill()
for i in range(5):
    t.forward(76)
    t.right(144)

t.end_fill()
#第五颗星
t.penup()

t.goto(-230,70)

t.pendown()

t.right(25)

t.begin_fill()
for i in range(5):
    t.forward(76)
    t.right(144)

t.end_fill()
