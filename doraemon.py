from turtle import *

import bold as bold

pen = Turtle()
pencolor('black')
pensize(3)

def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()
#head
my_goto(-40,80)
begin_fill()
fillcolor('dodger blue')
circle(100)
end_fill()
begin_fill()
fillcolor('white')
circle(80)
end_fill()

#eyes
begin_fill()
fillcolor('white')
my_goto(-70, 200)
circle(30, 380)
end_fill()

begin_fill()
fillcolor('white')
my_goto(-3, 200)
circle(30, 380)
end_fill()

#Black eyes
begin_fill()
fillcolor('black')
my_goto(-60, 220)
circle(12)
end_fill()

begin_fill()
fillcolor('black')
my_goto(-3, 220)
circle(12)
end_fill()

#lil White Eyes
begin_fill()
fillcolor('white')
my_goto(-63, 224)
circle(7)
end_fill()

begin_fill()
fillcolor('white')
my_goto(-6, 224)
circle(7)
end_fill()

#Nose
begin_fill()
fillcolor('red')
my_goto(-32, 180)
circle(15)
end_fill()

my_goto(-42, 192)
dot(7, 'white')
end_fill()
#straight line
my_goto(-42, 175)
rt(130)
fd(24)

#Mouth
begin_fill()
fillcolor('red')
my_goto(-92, 150)
circle(50, 180)
lt(90)
fd(100)
end_fill()
begin_fill()
fillcolor('orange red')
my_goto(-7, 116)
lt(320)
for i in range(75):
    lt(1.1)
    fd(1)
lt(100)
pensize(2)
for i in range(76):
    lt(1)
    fd(1)
end_fill()

#Beared left
pensize(3)
my_goto(-50, 152)
lt(160)
fd(60)

my_goto(-50, 160)
rt(20)
fd(60)

my_goto(-50, 168)
lt(-20)
fd(60)

#beared right
my_goto(-35, 152)
rt(180)
fd(60)

my_goto(-35, 160)
lt(20)
fd(60)

my_goto(-35,168)
rt(-20)
fd(60)

#body
begin_fill()
fillcolor('dodger blue')
my_goto(26, 108)
seth(20)
fd(70)
rt(90)
fd(35)
rt(70)
fd(95)
rt(120)
fd(20)
rt(180)
for i in range(140):
    rt(0.2)
    fd(1)
rt(71)
fd(40)
rt(90)
circle(23, 180)
rt(89)
fd(40)
rt(70)
for i in range(130):
    rt(0.3)
    fd(1)
rt(180)
fd(25)
rt(30)
fd(60)
rt(90)
fd(40)
rt(93)
fd(131)
rt(70)
circle(100, 73)

end_fill()

#Stomach
begin_fill()
fillcolor('white')
my_goto(-82.5, 74)
seth(226)
circle(60, 270)
rt(314)
fd(85)
end_fill()

#Belt
begin_fill()
fillcolor('red')
seth(18)
my_goto(-42, 90)
lt(-18)
fd(65)
right(90)
fd(15)
rt(90)
fd(130)
rt(90)
fd(15)
right(89)
fd(65)
end_fill()

#bell
begin_fill()
fillcolor('yellow')
my_goto(-42, 52)
circle(17.5)
end_fill()

my_goto(-55, 77)
fd(25)

my_goto(-42, 68)
dot(12, 'black')

my_goto(-42, 70)
right(90)
fd(17)

#Pocket
my_goto(-83, 37)
circle(45, 180)
lt(89)
fd(90)

#Hand
begin_fill()
fillcolor('white')
my_goto(100, 140)
circle(25)
end_fill()

begin_fill()
fillcolor('white')
my_goto(-180, 20)
circle(25)
end_fill()

#Leg Left
my_goto(-111, -82)
seth(185)
circle(17, 160)
rt(-15)
fd(45)
circle(17, 160)
fd(5)

#Leg Right
my_goto(-22, -82)
seth(185)
circle(17, 160)
rt(-15)
fd(45)
circle(17, 160)
fd(5)

my_goto(-10000, -1000000)
circle(8, 1000000)
hideturtle()
done