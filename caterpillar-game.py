import turtle as t
import random as rd

wn = t.getscreen()
t.bgcolor("black")

game_started = False

caterpillar = t.Turtle()
caterpillar.hideturtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.color("white")

leaf = t.Turtle()
leaf.hideturtle()
leaf.color("green")
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.penup()
leaf.speed()

text_turtle = False
text_turtle = t.Turtle()
text_turtle.color("white")
text_turtle.write("Press Space to Start", align="center", font=('Arial', 20, "bold"))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.color("white")
score_turtle.hideturtle()
score_turtle.speed(0)


def outsideWindow():
    left_limit = -t.window_width() / 2
    right_limit = t.window_height() / 2

    top_limit = t.window_height() / 2
    bottom_limit = -t.window_height() / 2
    x, y = caterpillar.pos()
    return left_limit > x or x > right_limit or bottom_limit > y or y > top_limit


def placeLeaf():
    leaf.hideturtle()
    x, y = rd.randint(-200, 200), rd.randint(-200, 200)
    leaf.setx(x)
    leaf.sety(y)
    leaf.showturtle()


def gameOver(current_score):
    caterpillar.hideturtle()
    leaf.hideturtle()
    t.penup()
    t.hideturtle()
    t.color("white")
    t.write("Game Over!!!\nYour Score : " + str(current_score), align="center", font=("Arial", 30, "bold"))


def displayScore(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = t.window_width() / 2 - 50
    y = t.window_height() / 2 - 100
    score_turtle.setpos(x, y)
    score_turtle.pendown()
    score_turtle.write(str(current_score), align="right", font=("Arial", 40, "bold"))


def startGame():
    global game_started
    if game_started:
        return

    game_started = True
    text_turtle.clear()

    caterpillar.speed = 2
    caterpillar.length = 3
    caterpillar.shapesize(1, caterpillar.length, 1)
    caterpillar.showturtle()
    current_score = 0
    displayScore(current_score=current_score)
    placeLeaf()
    # score_turtle.showturtle()

    while True:
        caterpillar.forward(caterpillar.speed)
        if caterpillar.distance(leaf.pos()) <= 25:
            placeLeaf()
            caterpillar.length = caterpillar.length + 1
            caterpillar.shapesize(1, caterpillar.length, 1)
            caterpillar.speed += 1
            current_score += 10
            displayScore(current_score)
        if outsideWindow():
            gameOver(current_score)
            break


def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)


def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)


def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)


def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)


t.onkey(startGame, 'space')

t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_right, 'Right')
t.onkey(move_left, 'Left')

t.listen()
t.mainloop()
