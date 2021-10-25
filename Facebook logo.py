from turtle import *
s = Screen()
s.bgcolor('black')
pensize(3)
pencolor('blue')
def my_goto(x,y):
    penup()
    goto(x,y)
    pendown()
begin_fill()
my_goto(0,-180)
fillcolor('blue')
circle(200)
end_fill()
pensize(40)
pencolor('white')
my_goto(0,-170)
lt(90)
fd(250)
circle(-70,100)
my_goto(-55,-20)
rt(-10)
fd(120)




my_goto(1000000,1000000)
circle(4)