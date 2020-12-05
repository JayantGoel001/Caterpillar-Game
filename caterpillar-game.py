import turtle as t
import random as rd

wn = t.getscreen()
t.bgcolor("black")

left_limit = -t.window_width() / 2 + 100
right_limit = t.window_height() / 2 - 100

top_limit = t.window_height() / 2 - 100
bottom_limit = -t.window_height() / 2 + 100

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
score_turtle.hideturtle()
score_turtle.speed(0)


def outsideWindow():
    x, y = t.pos()
    return not (left_limit < x < right_limit and bottom_limit < y < top_limit)


def placeLeaf():
    leaf.hideturtle()
    x, y = rd.randint(int(left_limit), int(right_limit)), rd.randint(int(bottom_limit), int(top_limit))
    leaf.setx(x)
    leaf.sety(y)
    leaf.showturtle()


def gameOver():
    caterpillar.hideturtle()
    leaf.hideturtle()
    t.penup()
    t.hideturtle()
    t.write("Game Over!!!", align="center", font=("Arial", 30, "bold"))


def displayScore(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = t.window_width() / 2 - 50
    y = t.window_height() / 2 - 50
    score_turtle.goto(x, y)
    score_turtle.pendown()
    score_turtle.write(str(current_score), align="right", font=("Arial", 40, "bold"))


def startGame():
    global game_started
    if game_started:
        return

    game_started = True
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    current_score = 0
    displayScore(current_score=current_score)
    placeLeaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            placeLeaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_speed, 1)
            caterpillar_speed += 1
            current_score += 10
            displayScore(current_score)
        if outsideWindow():
            gameOver()
            break


def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        pass


def move_down():
    pass


def move_right():
    pass


def move_left():
    pass


t.onkey(startGame, 'space')

t.onkey(move_up, 'up')
t.onkey(move_down, 'down')
t.onkey(move_right, 'right')
t.onkey(move_left, 'left')

t.listen()
t.mainloop()
