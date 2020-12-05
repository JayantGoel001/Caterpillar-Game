import turtle as t
import random as rd

wn = t.getscreen()
t.bgcolor("black")

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.color("white")
caterpillar.hideturtle()

leaf = t.Turtle()
leaf.color("green")
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.penup()
leaf.hideturtle()
leaf.speed()

text_turtle = False
text_turtle = t.Turtle()
text_turtle.color("white")
text_turtle.write("Press Space to Start", align="center", font=('Arial', 20, "bold"))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

wn.mainloop()

left_limit = -t.window_width() / 2 + 100
right_limit = t.window_height() / 2 - 100

top_limit = t.window_height() / 2 - 100
bottom_limit = -t.window_height() / 2 + 100


def outside_window():
    x, y = t.pos()
    return not (left_limit < x < right_limit and bottom_limit < y < top_limit)


def place_leaf():
    leaf.hideturtle()
    x, y = rd.randint(int(left_limit), int(right_limit)), rd.randint(int(bottom_limit), int(top_limit))
    leaf.setx(x)
    leaf.sety(y)
    leaf.showturtle()


def game_over():
    caterpillar.hideturtle()
    leaf.hideturtle()
    t.penup()
    t.hideturtle()
    t.write("Game Over!!!", align="center", font=("Arial", 30, "bold"))


def display_score():
    score_turtle.clear()
    score_turtle.penup()
    x = t.window_width() / 2 - 50
    y = t.window_height() / 2 - 50
    score_turtle.write(str(current_score), align="right", font=["Arial", 40, "bold"])
