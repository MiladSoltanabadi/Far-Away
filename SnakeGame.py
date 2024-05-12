import turtle
import time
import random

delay = 0.1
queue = []

# Calculate the score and high score
pen = turtle.Turtle()
pen.shape('square')
pen.penup()
pen.speed(0)
pen.color('White')

pen.hideturtle()
pen.goto(0, 310)
pen.write("Score: 0", align='center', font=('Arial', 25, 'bold'))

# Create Window
window = turtle.Screen()
window.bgcolor('black')
window.title('Mox Snake by Milad Soltani')
window.setup(width=900, height=700)
window.tracer(0)

# Create Snakes Head
snake_Head = turtle.Turtle()
snake_Head.speed(0)
snake_Head.shape('circle')
snake_Head.color('green')
snake_Head.penup()
snake_Head.goto(0, 0)  # Spawn snake in center
snake_Head.direction = 'stop'

# Create Food
snake_Food = turtle.Turtle()
snake_Food.speed(0)
snake_Food.shape('circle')

snake_Food.color('red')
snake_Food.penup()
snake_Food.goto(0, 150)


def Move_Snake():
    # Numbers are Snake Speed
    if snake_Head.direction == 'up':
        y = snake_Head.ycor()
        snake_Head.sety(y + 20)
    if snake_Head.direction == 'down':
        y = snake_Head.ycor()
        snake_Head.sety(y - 20)
    if snake_Head.direction == 'left':
        x = snake_Head.xcor()
        snake_Head.setx(x - 20)
    if snake_Head.direction == 'right':
        x = snake_Head.xcor()
        snake_Head.setx(x + 20)


def go_up():
    snake_Head.direction = 'up'


def go_down():
    snake_Head.direction = 'down'


def go_left():
    snake_Head.direction = 'left'


def go_right():
    snake_Head.direction = 'right'


def Food_Collision():
    if snake_Head.distance(
            snake_Food) < 30:
        snake_Food.goto(random.randint(-438, 432), random.randint(-330, 330))
        # use random numbers for spawn foods
        snake_body = turtle.Turtle()
        snake_body.speed(0)
        snake_body.shape('circle')
        snake_body.color('red')
        snake_body.penup()
        queue.append(snake_body)
        return True
    return False


def Border_Collision():
    # Border collision
    if snake_Head.xcor() > 435 or snake_Head.xcor() < -440 or snake_Head.ycor() > 340 or snake_Head.ycor() < -335:
        time.sleep(1)
        snake_Head.goto(0, 0)
        snake_Head.direction = 'stop'

        for segment in queue:
            segment.goto(1000, 1000)
        queue.clear()
        return True

    return False


def Body_Collision():
    # body collisions
    for segment in queue:
        if segment.distance(snake_Head) < 10:  # overlapping
            time.sleep(1)
            snake_Head.goto(0, 0)
            snake_Head.direction = 'stop'
            for segment in queue:
                segment.goto(1000, 1000)
            queue.clear()
            return True
    return False


def Add_Snake_Body():
    # add body to the snake iterate from the last one in the list
    for i in range(len(queue) - 1, 0, -1):
        if i % 5 == 0:
            queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
            queue[i].color('green')
            continue
        queue[i].goto(queue[i - 1].xcor(), queue[i - 1].ycor())
    if len(queue) > 0:
        queue[0].goto(snake_Head.xcor(), snake_Head.ycor())


# Keyboard keys
window.listen()
window.onkeypress(go_up, 'Up')
window.onkeypress(go_down, 'Down')
window.onkeypress(go_left, 'Left')
window.onkeypress(go_right, 'Right')


score = 0
High_Score = 0
while True:
    # Game Loop
    window.update()
    Move_Snake()
    if Food_Collision():
        score += 1
        pen.clear()
        pen.write(f'Score:{score} ', align='center', font=('Arial', 25, 'bold'))

    if Body_Collision() or Border_Collision():
        score = 0
        pen.clear()
        pen.write(f'Score:{score}  ', align='center', font=('Arial', 25, 'bold'))
    time.sleep(delay)
    Add_Snake_Body()
