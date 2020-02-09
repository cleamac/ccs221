import turtle

window=turtle.Screen()
window.bgcolor("#000000")
glecy=turtle.Turtle()
glecy.up()
glecy.setpos(-80,80)
glecy.down()
glecy.color("red")
glecy.width(2)

def G(g):
    g.backward(30)
    g.left(40)
    g.backward(20)
    g.left(50)
    g.backward(40)
    g.left(50)
    g.backward(20)
    g.right(140)
    g.forward(30)
    g.left(40)
    g.forward(20)
    g.left(50)
    g.forward(20)
    g.left(90)
    g.forward(30)

def L(l):
    l.up()
    l.backward(35)
    l.left(90)
    l.backward(37)
    l.down()
    l.forward(70)
    l.left(90)
    l.forward(40)

def E(e):
    e.up()
    e.forward(5)
    e.down()
    e.left(90)
    e.forward(70)
    e.right(90)
    e.forward(40)
    e.up()
    e.right(90)
    e.forward(36)
    e.down()
    e.right(90)
    e.forward(40)
    e.up()
    e.left(90)
    e.forward(35)
    e.left(90)
    e.down()
    e.forward(40)

def C(c):
    c.up()
    c.forward(5)
    c.left(90)
    c.down()
    c.forward(71)
    c.right(90)
    c.forward(40)
    c.up()
    c.right(90)
    c.forward(71)
    c.right(90)
    c.down()
    c.forward(40)

def Y(y):
    y.up()
    y.backward(45)
    y.left(90)
    y.backward(71)
    y.down()
    y.left(40)
    y.forward(50)
    y.left(140)
    y.backward(35)
    y.up()
    y.forward(35)
    y.left(140)
    y.down()
    y.backward(50)

G(glecy)
L(glecy)
E(glecy)
C(glecy)
Y(glecy)
glecy.hideturtle()

turtle.done()
