import random

import pgzrun
from pgzero.actor import Actor

TITLE = "Arkanoid clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

ball_x_speed = 1
ball_y_speed = 1

bars_list = []
color_list = []

RED = 0
BLUE = 0
GREEN = 0


def draw():
    screen.blit("background.png", (0, 0))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()


def place_bars(x,y,image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)
        color_list.append(image)


def update():
    global ball_x_speed, ball_y_speed, BLUE, GREEN, RED
    if keyboard.left:
        paddle.x = paddle.x - 6
    if keyboard.right:
        paddle.x = paddle.x + 6

    update_ball()

    for bar in bars_list:
        if ball.colliderect(bar):
            bar_index = bars_list.index(bar)
            print('index =', bar_index)
            bars_list.remove(bar)
            ball_y_speed *= -1
            bar_color = color_list[bar_index]
            if bar_color == 'element_blue_rectangle_glossy.png':
                BLUE += 2
            if bar_color == 'element_green_rectangle_glossy.png':
                GREEN += 3
            if bar_color == 'element_red_rectangle_glossy.png':
                RED += 1

    if paddle.colliderect(ball):
        ball_y_speed *= -1
        # randomly move ball left or right on hit
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1

def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <= 0):
        ball_x_speed *= -1
    if ball.y <= 0:
        ball_y_speed *= -1
    if ball.y >= HEIGHT:
        print('Game Over')
        print('Score = ',(RED + GREEN + BLUE))
        ball_y_speed *= -1



coloured_box_list = [
    "element_blue_rectangle_glossy.png",
    "element_green_rectangle_glossy.png",
    "element_red_rectangle_glossy.png"
]
x = 120
y = 100

for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()
