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
