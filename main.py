import random

import pgzrun
from vector import Vector
from pgzero.actor import Actor

# from vector import Vector


class Circle:
    def __init__(self, vector: Vector):
        self. position = vector
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)


# class Coin:
#     def __init__(self, vector:Vector):
#         self.position = vector
#         self.velocity = Vector(0, 0)
#         self.acceleration = Vector(0, 0)
#
#     def draw(self):
#         screen.draw.circle((self.position.x, self.position.y), 50, "yellow")
#
#     def move(self,dt):
#         self.position += self.velocity * dt


WIDTH = 800
HEIGHT = 800
RADIUS = 50

circle = Circle(Vector(200, 200))
gravity = Vector(0, 20)
# coins = []



def draw():
    screen.clear()
    screen.draw.circle((circle.position.x, circle.position.y), 50, "yellow")
    # for coin in coins:
    #     coin.draw()


def update(dt): # 1/60s
    circle.acceleration += gravity
    circle.velocity += circle.acceleration
    v = circle.velocity
    circle.acceleration = Vector(0, 0)

    if circle.position.y >= HEIGHT - RADIUS and v.y > 0:
        circle.velocity = Vector(v.x, -v.y)
    circle.position += Vector(v.x * dt, v.y * dt)    # if random.random() < 0.05:
    #     position = Vector(random.randint(0, WIDTH), 0)
    #     coins.append(Coin(position))
    # for coin in coins:
    #     coin.move(dt)


pgzrun.go()
