import turtle
import random

# define consts
width = 1000
height = 1000
delay = 200
food_size = 25

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

    # check collision
    if new_head in snake or new_head[0] < - width / 2 or new_head[0] > width / 2 or new_head[1] < - height / 2 or \
            new_head[1] > height / 2:
        turtle.bye()
    else:
        # add new head to snake
        snake.append(new_head)

        # check food collision
        if not food_collision():
            snake.pop(0)  # stay same

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # refresh screen
        screen.title(f"snake game Score: {score}")
        screen.update()
        # rinse and reset
        turtle.ontimer(game_loop, delay)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food()
        food.goto(food_pos)
        return True
    return False


def get_random_food():
    x = random.randint(- width / 2 + food_size, width / 2 - food_size)
    y = random.randint(- height / 2 + food_size, height / 2 - food_size)
    return x, y


# теорема Пифагора
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


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
score = 0

# draw snake first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# food
food = turtle.Turtle()
food.shape("circle")
food.color("blue")
food.shapesize(food_size / 20)
food.penup()
food_pos = get_random_food()
food.goto(food_pos)

# set anim in motion
game_loop()

# finish
turtle.done()
