import turtle
t=turtle.Pen()

t.penup()
t.goto(-270,0)
t.pendown()
####Letra J
t.color(0,1,0)
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(100)
t.left(180)
t.left(90)
t.forward(40)
t.left(90)
t.forward(20)  
t.right(270)
t.forward(100)
t.right(270)
t.forward(20)
t.right(270)
t.forward(40)
t.left(270)
t.forward(80)
t.left(270)
t.forward(30)
t.right(270)
t.forward(20)
t.end_fill()
###Letra O
t.setheading(0)
t.penup()
t.goto(-170,0)
t.pendown()

t.color(0,1,0)
t.begin_fill()
t.right(270)
t.forward(120)
t.left(270)
t.forward(60)
t.left(270)
t.forward(120)
t.left(270)
t.forward(60)
t.end_fill()

t.setheading(0)
t.penup()
t.goto(-150,20)
t.pendown()

t.begin_fill()
t.color(1,1,1)
t.right(270)
t.forward(80)
t.left(270)
t.forward(20)
t.left(270)
t.forward(80)
t.left(270)
t.forward(20)
t.end_fill()
###Letra R
t.setheading(0)
t.penup()
t.goto(-100,0)
t.pendown()

t.color(0,1,0)
t.begin_fill()
t.right(270)
t.forward(120)
t.left(270)
t.forward(60)
t.left(270)
t.forward(60)
t.left(290)
t.forward(15)
t.right(270)
t.forward(60)
t.left(290)
t.setheading(0)
t.left(180)
t.forward(20)
t.left(290)
t.forward(60)
t.left(80)
t.forward(8)
t.right(280)
t.forward(55)
t.left(270)
t.forward(20)
t.end_fill()

t.setheading(0)
t.penup()
t.goto(-80,75)
t.pendown()
a=6
t.color(0,1,0)
t.begin_fill()
for x in range(a):
        
        t.forward(15)
        t.right((a-2)*180/a)
        t.right((a-2)*270/a)
t.end_fill()

###G
t.setheading(0)
t.penup()
t.goto(-20,0)
t.pendown()

t.color(0,1,0)
t.begin_fill()
t.right(270)
t.forward(120)
t.left(270)
t.forward(60)
t.left(270)
t.forward(40)
t.left(270)
t.forward(20)
t.left(270)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(80)
t.left(90)
t.forward(20)
t.left(90)
t.forward(15)
t.left(90)
t.forward(15)
t.left(270)
t.forward(20)
t.right(90)
t.forward(35)
t.right(90)
t.forward(55)
t.right(90)
t.forward(60)
t.end_fill()
###E
t.setheading(0)
t.penup()
t.goto(50,0)
t.pendown()

t.color(0,1,0)
t.begin_fill()
t.right(270)
t.forward(120)
t.left(270)
t.forward(60)
t.left(270)
t.forward(20)
t.left(270)
t.forward(40)
t.left(90)
t.forward(30)
t.left(90)
t.forward(30)
t.left(270)
t.forward(20)
t.left(270)
t.forward(30)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.left(270)
t.forward(20)
t.left(270)
t.forward(60)
t.end_fill()
