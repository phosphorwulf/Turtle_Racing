"""
  _________  __  __ _____  _____   ______ __  __ _____  ______ __ __ __ __  __ __     ______
  \_  ___  // / / // __  // ____\ \ __  // / / // __  // __  // // // // / / // /    / ____/
   / /__/ // /_/ // / / // /__   / /_/ // /_/ // / / // /_/ // // // // / / // /    / /__
  / _____// __  // / / / \___ \ / ____// __  // / / // _  _// // // // / / // /    / ___/
 / /     / / / // /_/ /_____/ // /    / / / // /_/ // / \ \ \ V  V // /_/ // /___ / /
/_/     /_/ /_//_____//______//_/    /_/ /_//_____//_/  \_\ \__/\_/\_____//_____//_/
"""

import turtle
import time
import random

WIDTH, HEIGHT = 900, 600
RACERS = 5

COLORS = ['green', 'red', 'blue', 'orange', 'purple']

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = int(random.randrange(1,20))
            racer.speed(int(distance / 2))
            racer.forward(distance)

            x, y = racer.pos()
            if x >= WIDTH // 2 - 15:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacing = HEIGHT // (len(colors) +1)
    print(colors)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.resizemode("user")
        racer.shapesize(stretch_wid=3, stretch_len=3, outline=1)
        #racer.resizemode(stretch_wid=10, stretch_len=10, outline=10)
        racer.color(color)
        racer.shape('turtle')
        racer.left(360)
        racer.penup()
        racer.setpos(-WIDTH // 2 + 10, -HEIGHT // 2 + (int(len(colors)) - i) * spacing)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    # Set screen for canvas
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("moccasin")
    screen.title('Turtle Race!!')

init_turtle()

colors = COLORS[:RACERS]
winner = race(colors)
turtle.hideturtle()
turtle.color(winner)
turtle.write("The " + winner + " turtle wins!!", font=("Courier New", 30, "bold"), align="center")
time.sleep(5)
