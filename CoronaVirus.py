from turtle import *
color('green')
bgcolor('black')
speed(10)
up()
goto(-20,150)
down()
b = 0
while b < 200:
    rt(b)
    fd(b*3)
    b = b+1
hideturtle()
done