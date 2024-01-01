import random
import matplotlib.pyplot as plt


def plot(points):
    """
    Plots the points using matplotlib.
    Points is a list of (x, y) pairs.
    """

    xx = [x for (x, y) in points]
    yy = [y for (x, y) in points]

    plt.plot(xx, yy, 'g.')
    plt.show()


def sierpinski(n):
    """
    Generates positions for the Chaos Game Sierpinski
    triangle with 'n iterations in a square of size 1x1.
    """

    vertices = [(0.0, 0.0), (0.5, 1.0), (1.0, 0.0)]
    points = []

    # initial vertex
    x, y = random.choice(vertices)

    for i in range(n):
        # select new vertex
        vx, vy = random.choice(vertices)

        # get middle point
        x = (vx + x) / 2.0
        y = (vy + y) / 2.0

        points.append((x, y))

    plot(points)

