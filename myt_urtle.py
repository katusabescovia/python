import turtle

def draw_circle(color, x, y, radius):
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    tr.color(color)
    tr.circle(radius)

def draw_olympic():
    colors = ["blue", "black", "red", "yellow", "green"]
    positions = [(-110, -25), (0, -25), (110, -25), (-55, -75), (55, -75)]
    radius = 45
    
    for color, position in zip(colors, positions):
        draw_circle(color, position[0], position[1], radius)


tr = turtle.Turtle()
tr.pensize(5)

draw_olympic()


