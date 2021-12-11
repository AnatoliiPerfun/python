import turtle

# define consts
width = 1000
height = 1000
delay = 300


def move_snake():
    stamper.clearstamps()  # remove existing stamps

    new_head = snake[-1].copy()
    new_head[0] += 20
    # add new head to snake
    snake.append(new_head)
    # remove tale of snake
    snake.pop(0)
    # draw snake first time
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()
    # refresh screen
    screen.update()
    # rinse and reset
    turtle.ontimer(move_snake, delay)


# create window
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake game")
screen.bgcolor("pink")
screen.tracer(0)

# create a turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# create snake
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# draw snake first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# set anim in motion
move_snake()

# finish
turtle.done()
