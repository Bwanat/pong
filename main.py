import turtle

#intestazioni
size = [640,480]
run = True
score_a = 0
score_b=0

win = turtle.Screen()
win.title ('Donkey Pong')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

#palyer_a
palyer_a = turtle.Turtle()
palyer_a.speed(0)
palyer_a.shape('square')
palyer_a.color('white')
palyer_a.shapesize(stretch_wid=5, stretch_len=1)
palyer_a.penup()
palyer_a.goto(-350,0)

#palyer_b
palyer_b = turtle.Turtle()
palyer_b.speed(0)
palyer_b.shape('square')
palyer_b.color('white')
palyer_b.shapesize(stretch_wid=5, stretch_len=1)
palyer_b.penup()
palyer_b.goto(350,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = -1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('PlayerA: 0 - 0 PlayerB', align='center', font=('Courier', 24, 'normal'))

#function

def paup():
    y=palyer_a.ycor()
    y += 20
    palyer_a.sety(y)

def padow():
    y=palyer_a.ycor()
    y -= 20
    palyer_a.sety(y)

def pbup():
    y=palyer_b.ycor()
    y += 20
    palyer_b.sety(y)

def pbdow():
    y=palyer_b.ycor()
    y -= 20
    palyer_b.sety(y)


#key binding
win.listen()
win.onkeypress(paup, 'w')
win.onkeypress(padow, 's')
win.onkeypress(pbup, 'Up')
win.onkeypress(pbdow, 'Down')

#loop
while True:
    win.update()

    #moveball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write('PlayerA: {} - {} PlayerB'.format(score_a,score_b),align='center', font=('Courier', 24, 'normal'))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write('PlayerA: {} - {} PlayerB'.format(score_a,score_b),align='center', font=('Courier', 24, 'normal'))


    #paddle and ball collision

    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < palyer_b.ycor()+50 and ball.ycor() > palyer_b.ycor() -50):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < palyer_a.ycor()+50 and ball.ycor() > palyer_a.ycor() -50):
        ball.setx(-340)
        ball.dx *=-1
