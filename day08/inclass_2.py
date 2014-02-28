from swampy.TurtleWorld import *
from math import pi

def my_triangle(turtle, side_length):
    fd(turtle, side_length)
    lt(turtle, 120)
    fd(turtle, side_length)
    lt(turtle, 120)
    fd(turtle, side_length)

"""
- Move position
alice.x = 100
alice.y = -50
alice.heading = 200
"""

################################################################################
#
################################################################################

"""
1. Write a function called my_square that
takes as input the coordinates of the lower lefthand corner and the side length of a square
and
draws the square to the Turtle world canvas.
"""

#world = TurtleWorld()
#bob = Turtle()
#bob.delay = .001

def my_square(x, y, side_length):
    bob.x = x
    bob.y = y
    fd(bob, side_length)
    lt(bob, 90)
    fd(bob, side_length)
    lt(bob, 90)
    fd(bob, side_length)
    lt(bob, 90)
    fd(bob, side_length)

def my_square2(x, y, side_length):
    bob.x = x
    bob.y = y
    #for i in range(3):
    for i in range(4):
        fd(bob, side_length)
        lt(bob, 90)
    #fd(bob, side_length)

"""
2. Write a function called my_regular_polygon that
takes as input the lower lefthand vertex, the side length, and the number of sides of a regular polygon
and
draws the polygon to the Turtle world canvas.
"""
def my_regular_polygon(v, side_length, num_sides):
    # v is a list, [x, y]
    bob.x = v[0]
    bob.y = v[1]
    bob.heading = 0
    for i in range(num_sides):
        fd(bob, side_length)
        lt(bob, (360 / num_sides))

"""
3. Modify your my_square function so that it uses my_regular_polygon
"""
def my_square_modified(x, y, side_length):
    my_regular_polygon([x, y], side_length, 4)

"""
4. Write a function called my_circle that
takes as input the center and radius of a circle and
draws the circle to the canvas by approximating a circle as a regular polygon of a large number of sides.
In order to figure out the side length to use for the regular polygon make sure that  n*side_length = 2*pi*radius (where n is the number of sides of the polygon that you use to approximate the circle).  Make sure to use my_regular_polygon when writing this function.
"""
def my_circle(center, radius):
    my_regular_polygon(center, 2.0 * pi * radius / 40, 40)

################################################################################
#
################################################################################

def snow_flake_side(turtle, l, level):
    """ Draw a side of the snowflake curve with side length l and recursion depth of level """
    if level == 1:
        fd(turtle, l)
        rt(turtle, 60)
        fd(turtle, l)
        lt(turtle, 60 * 2)
        fd(turtle, l)
        rt(turtle, 60)
        fd(turtle, l)
        return
    snow_flake_side(turtle, l / 3.0, level - 1)
    rt(turtle, 60)
    snow_flake_side(turtle, l / 3.0, level - 1)
    lt(turtle, 60 * 2)
    snow_flake_side(turtle, l / 3.0, level - 1)
    rt(turtle, 60)
    snow_flake_side(turtle, l / 3.0, level - 1)

################################################################################
#
################################################################################

# sf: snow flake
def my_regular_polygon_4_sf(turtle, side_length, num_sides):
    turtle.heading = 0
    for i in range(num_sides):
        #fd(turtle, side_length)
        snow_flake_side(turtle, side_length, 2)
        lt(turtle, (360 / num_sides))

def my_circle_4_sf(turtle, l, num_sides):
    my_regular_polygon_4_sf(turtle, l, num_sides)

def snow_flake(turtle, l, num_sides):
    my_circle_4_sf(turtle, l, num_sides)

################################################################################
#
################################################################################
def clone_turtle(turtle):
    new_turtle = Turtle()
    new_turtle.x = turtle.x
    new_turtle.y = turtle.y
    new_turtle.heading = turtle.heading
    new_turtle.pen_color = turtle.pen_color
    return new_turtle

def recursive_tree(turtle, branch_length, level):
    """ Draw a tree with branch length branch_length and recursion depth of level """
    ###############
    # Base
    ###############
    # Draw line
    fd(turtle, branch_length)
    if (level == 1): return
    ###############
    # 1st branch (left)
    ###############
    # Clone turtle
    new_turtle = clone_turtle(turtle)
    new_turtle.lt(30)
    # Call
    recursive_tree(new_turtle, branch_length * 0.6, level - 1)
    # Undraw cloned one
    new_turtle.undraw()
    # Go backward
    turtle.bk(branch_length / 3.0)
    ###############
    # 2nd branch (right)
    ###############
    # Clone turtle
    new_turtle = clone_turtle(turtle)
    new_turtle.rt(40)
    # Call
    recursive_tree(new_turtle, branch_length * 0.64, level - 1)
    # Undraw cloned one
    new_turtle.undraw()

if __name__ == "__main__":
    """world = TurtleWorld()
    alice = Turtle()
    my_triangle(alice, 30)
    wait_for_user()"""

    #my_square(0, 0, 30)
    #my_square2(50, 50, 30)

    #my_regular_polygon([0, 0], 30, 12)
    #my_regular_polygon([0, 0], 30, 8)

    #my_square_modified(0, 0, 40)

    #my_circle([0, 0], 100)

    #bob.x = -70
    #bob.y = -70
    #snow_flake_side(bob, 50, 5)

    #bob.x = -70
    #bob.y = -70
    #snow_flake(bob, 15, 20)

    world = TurtleWorld()
    turtle = Turtle()
    turtle.delay = 0.001
    turtle.pen_color = "green"
    turtle.x = -100
    turtle.y = -100
    turtle.heading = 90
    recursive_tree(turtle, 100, 10)

    wait_for_user()