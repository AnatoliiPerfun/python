import turtle

# define consts
width = 1000
height = 1000
delay = 200

offset = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}


def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"


def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"


def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"


def game_loop():
    stamper.clearstamps()  # remove existing stamps

    new_head = snake[-1].copy()
    new_head[0] += offset[snake_direction][0]
    new_head[1] += offset[snake_direction][1]

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
    turtle.ontimer(game_loop, delay)


# create window
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake game")
screen.bgcolor("pink")
screen.tracer(0)

# event handlers
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# create a turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()

# create snake
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"

# draw snake first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# set anim in motion
game_loop()

# finish
turtle.done()
