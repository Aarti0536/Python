import turtle
pen = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
pen.color('blue','blue')
pen.pensize(7)
pen.hideturtle()
pen.fd(120)
pen.right(90)
pen.circle(-150,50)
pen.color('green')
pen.circle(-150,100)
pen.color('yellow')
pen.circle(-150,60)
pen.color('red','red')
pen.begin_fill()
pen.circle(-150,100)
pen.right(90)
pen.fd(50)
pen.right(90)
pen.circle(100,100)
pen.right(90)
pen.fd(50)
pen.end_fill()

pen.begin_fill()
pen.color('yellow','yellow')
pen.right(180)
pen.fd(50)
pen.right(90)
pen.circle(100,60)
pen.right(90)
pen.fd(50)
pen.right(90)
pen.circle(-150,60)
pen.end_fill()

pen.right(90)
pen.fd(50)
pen.right(90)
pen.circle(100,60)
pen.begin_fill()
pen.color('green','green')
pen.right(90)
pen.fd(50)
pen.left(90)
pen.circle(150,100)
pen.left(90)
pen.fd(50)
pen.left(90)
pen.circle(-100,100)
pen.end_fill()
pen.left(90)
pen.fd(50)
pen.left(90)
pen.circle(150,100)
pen.left(90)
pen.fd(50)
pen.right(90)

pen.color('blue','blue')
pen.begin_fill()
pen.circle(100,25)
pen.left(115)
pen.fd(65)
pen.right(90)
pen.fd(42)
pen.right(90)
pen.fd(124)
pen.right(90)
pen.circle(-150,50)
pen.right(90)
pen.fd(50)
pen.end_fill()

turtle.done()