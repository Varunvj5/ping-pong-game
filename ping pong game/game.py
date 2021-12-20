import turtle as t
# Scores of the players
PlayerAscore = 0
PlayerBscore = 0

# Creating game screen
window = t.Screen()
window.title("Ping Pong Game")
window.bgcolor("black")
window.setup(width = 800 , height = 600,)
window.tracer

# Creating left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid = 5,stretch_len = 1)
leftpaddle.penup()
leftpaddle.goto(-350,0) 

# Creating right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid = 5,stretch_len = 1)
rightpaddle.penup()
rightpaddle.goto(350,0)

# Creating a ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,5)
ballxdirection = 8
ballydirection = 8

# Creating card for score update
card = t.Turtle()
card.speed()
card.color("green")
card.penup()
card.hideturtle()
card.goto(0,260)
card.write("SCORE",align = "center",font = ("Times New Roman",24,"normal"))

# Moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y+80
    leftpaddle.sety(y)
    
def leftpaddledown():
    y = leftpaddle.ycor()
    y = y-80
    leftpaddle.sety(y)

# Moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y+80
    rightpaddle.sety(y)
    
def rightpaddledown():
    y = rightpaddle.ycor()
    y = y-80
    rightpaddle.sety(y)
    
# Assigning keys to play
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'8')
window.onkeypress(rightpaddledown,'2')

# Declaring main game loop
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Setting up the boundary
    if ball.ycor()>290: 
        ball.sety(290)
        ballydirection = ballydirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection = ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection = ballxdirection*-1
        PlayerAscore = PlayerAscore+1
        card.clear()
        card.write("Player A:{}      Player B:{}".format(PlayerAscore,PlayerBscore),align ='center',font =('Chiller',24,'normal'))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection = ballxdirection*-1
        PlayerBscore = PlayerBscore+1
        card.clear()
        card.write("Player A:{}      Player B:{}".format(PlayerAscore,PlayerBscore),align ='center',font =('Chiller',24,'normal'))

    # Handling the collisions
    if (ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(340)
        ballxdirection = ballxdirection*-1

    if (ball.xcor()<-340) and (ball.xcor()>-350) and (ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-340)
        ballxdirection = ballxdirection*-1




