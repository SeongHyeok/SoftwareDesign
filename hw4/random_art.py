# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: SeongHyeok Im
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import cos, sin, pi
import time

"""
function_list: global variable for storing list of functions

prod(a,b) = ab
cos_pi(a) = cos(pi*a)
sin_pi(a) = sin(pi*a)
x(a,b) = a
y(a,b) = b
rev(a) = (-1)*a
half(a) = (0.5)*a
"""
function_list = [
    ["prod", "a", "b"],
    ["cos_pi", "a"],
    ["sin_pi", "a"],
    ["x", "a", "b"],
    ["y", "a", "b"],
    ["rev", "a"],
    ["half", "a"]
]

letter_by_position = [["x"], ["y"]]

def make_function(min_depth, max_depth, current_depth, position):
    """ Generate random function by using recursion.

        min_depth: the minimum amount of nesting for the generated function
        max_depath: the maximum amount of nesting of the generated function
        current_depth: current amount of nesting of the generated function
        position: indicates first argument(x) or second argument(y)
        returns: generated random function or just argument(x or y)
    """
    if current_depth >= min_depth:
        if randint(min_depth, max_depth) == min_depth:  # probability: 1 / (max_depth - min_depth)
            return letter_by_position[position]
    if current_depth == max_depth:
        return letter_by_position[position]

    v = randint(0, len(function_list) - 1)
    f = function_list[v]

    if len(f) == 2:     # only one argument
        return [
            f[0],
            make_function(min_depth, max_depth, current_depth + 1, 0)
        ]
    elif len(f) == 3:   # two arguments
        return [
            f[0],
            make_function(min_depth, max_depth, current_depth + 1, 0),
            make_function(min_depth, max_depth, current_depth + 1, 1)
        ]

def build_random_function(min_depth, max_depth):
    """ Create random function by calling make_function().

        min_depth: the minimum amount of nesting for the generated function
        max_depath: the maximum amount of nesting of the generated function
        returns: generated random function
    """
    return make_function(min_depth, max_depth, 1, 0)


def evaluate_random_function(f, x, y):
    """ Evaluate random function, f with given x and y using recursion.

        f: the random function to evaluate
        x: the value of x to evaluate the function
        y: the value of y to evaluate the function
        returns: evaluated value
    """
    if f[0] == "prod":
        return evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y)
    elif f[0] == "cos_pi":
        return cos(pi * evaluate_random_function(f[1], x, y))
    elif f[0] == "sin_pi":
        return sin(pi * evaluate_random_function(f[1], x, y))
    elif f[0] == "x":
        if len(f) == 1: # if "x" is alone
            return x
        return evaluate_random_function(f[1], x, y)
    elif f[0] == "y":
        if len(f) == 1: # if "y" is alone
            return y
        return evaluate_random_function(f[2], x, y)
    elif f[0] == "rev":
        return (-1.0) * evaluate_random_function(f[1], x, y)
    elif f[0] == "half":
        return (0.5) * evaluate_random_function(f[1], x, y)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).

        val: the value to be mapped
        input_interval_start: start value of input interval
        input_interval_end: end value of input interval
        output_interval_start: start v alue of output interval
        output_interval_end: end v alue of output interval
    """
    # [input] --> [output]
    input_interval = float(input_interval_end) - float(input_interval_start)
    output_interval = float(output_interval_end) - float(output_interval_start)
    return output_interval_start + \
            (output_interval) * ( (float(val) - input_interval_start) / input_interval )

def test1():
    f = build_random_function(3, 3)
    print f
    print evaluate_random_function(f, 0.5, 0.5)
    print remap_interval(50.0, 0.0, 200.0, 0.0, 1.0)
    print remap_interval(10, 0, 10, 100, 200)
    print remap_interval(10, 0, 100, -1, 1)

def step_1(min_depth, max_depth):
    red = build_random_function(min_depth, max_depth)
    green = build_random_function(min_depth, max_depth)
    blue = build_random_function(min_depth, max_depth)
    return red, green, blue

def test_step_1():
    red, green, blue = step_1(3, 5)
    print red, "//", green, "//", blue

def step_2(width, height):
    """ This function includes step 2, 3 and 4 of Part 3 in HW4
        Reference:
            http://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
            http://effbot.org/imagingbook/image.htm

        width: width of image
        height: height of image
    """
    img = Image.new("RGB", (width, height), "black")
    pixels = img.load()

    red, green, blue = step_1(5, 10)

    for x in range(width):
        rmx = remap_interval(x, 0, width - 1, -1, 1)
        for y in range(height):
            rmy = remap_interval(y, 0, width - 1, -1, 1)
            r = evaluate_random_function(red, rmx, rmy)
            g = evaluate_random_function(green, rmx, rmy)
            b = evaluate_random_function(blue, rmx, rmy)
            r = int(remap_interval(r, -1, 1, 0, 255))
            g = int(remap_interval(g, -1, 1, 0, 255))
            b = int(remap_interval(b, -1, 1, 0, 255))
            pixels[x, y] = (r, g, b)
    img.save("my_" + str(int(time.time())) + ".jpg", "JPEG")

def test_step_2():
    step_2(400, 400)

if __name__ == "__main__":
    #test1()
    #test_step_1()
    test_step_2()