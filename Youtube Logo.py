from turtle import *
s = Screen()
s.bgcolor('black')
pensize(5)
pencolor('red')

def my_goto(x,y):
    penup()
    goto(x,y)
    pendown()
my_goto(-180,120)
begin_fill()
fillcolor('red')
fd(300)
circle(-60,90)
fd(150)
circle(-60,90)
fd(300)
circle(-60,90)
fd(150)
circle(-60,90)
end_fill()

begin_fill()
my_goto(-90,80)
fillcolor('white')
pensize(2)
pencolor('white')
rt(90)
fd(180)
rt(-120)
fd(180)
rt(-120)
fd(180)
end_fill()


my_goto(100000,100000)
for i in range(10000):
    circle(3)


