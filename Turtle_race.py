import turtle as t
import random

t.hideturtle()

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5 = t.Turtle()
t6 = t.Turtle()
t7 = t.Turtle()

t_list = [t1,t2,t3,t4,t5,t6,t7]

t1.shape("turtle")
t1.color("blue")
t2.shape("turtle")
t2.color("green")
t3.shape("turtle")
t3.color("red")
t4.shape("turtle")
t4.color("grey")
t5.shape("turtle")
t6.shape("turtle")
t6.color("pink")
t7.shape("turtle")
t7.color("yellow")

t.penup()
t1.penup()
t1.goto(-300,-200)
t1.pendown()
t2.penup()
t2.goto(-200,-200)
t2.pendown()
t3.penup()
t3.goto(-100,-200)
t3.pendown()
t4.penup()
t4.goto(0,-200)
t4.pendown()
t5.penup()
t5.goto(100,-200)
t5.pendown()
t6.penup()
t6.goto(200,-200)
t6.pendown()
t7.penup()
t7.goto(300,-200)
t7.pendown()

t1.left(90)
t2.left(90)
t3.left(90)
t4.left(90)
t5.left(90)
t6.left(90)
t7.left(90)

#t1.forward(400)
#t2.forward(400)
#t3.forward(400)
#t4.forward(400)
#t5.forward(400)
#t6.forward(400)
#t7.forward(400)

while True:
    for i in random.choices(t_list):
        i.forward(3)
        #print(i.ycor())
    if i.ycor() == 220.0:
        break

t.home()


t.done()