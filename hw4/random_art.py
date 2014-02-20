# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from __future__ import division
from random import randint
import Image
from math import *
import math


def build_random_function(min_depth, max_depth):
    """inputs min_depth and max_depth.  The min_depth specifies the minimum amount 
    of nesting for the function and the max_depth specifies the maximum amount
    of nesting of the function. 
    
    returns a random  in a list    
    """
    n = randint(min_depth, max_depth)       # generating a random number between min and max to determine the depth for each case
    if n == 1:                              # base case when depth is equal to 1
        if randint(0,1) == 0:               # randomly choosing between treturning x and y
            return ["x"]
        else:      
            return ["y"]
    elif n>1:
        rand = randint(0,4)                 # generate a random integer to choose a function
        if rand == 0:
            return ["sin_pi" , build_random_function(n-1, n-1)]     # recurse by subtract n-1 (depth-1)
        elif rand == 1:
            return ["cos_pi", build_random_function(n-1, n-1)]
        elif rand == 2:
            return ["prod", build_random_function(n-1, n-1),build_random_function(n-1, n-1)]  # recursing twice because product requires two functions
        elif rand == 3:
            return ["avg", build_random_function(n-1, n-1),build_random_function(n-1, n-1)]
        elif rand == 4:
            return ["square", build_random_function(n-1, n-1),build_random_function(n-1, n-1)]
    
    
def evaluate_random_function(f, x, y):
    """ Input a random function f, a value of x and y where x and y are values between -1 and 1.
        Evaulates the function with the give values of x and y
    
        returns a value for the function    
    """
    if f[0] == "x":             # base case checking for x
        return x
    elif f[0] == "y":           # base case checking for y
        return y
    else:                       
        if f[0] == "sin_pi":
            return sin(pi*evaluate_random_function(f[1],x, y))  # evaulate recusion by looking at the next value on the list F[0]
        if f[0] == "cos_pi":
            return cos(pi*evaluate_random_function(f[1],x, y))
        if f[0] == "prod":
            return evaluate_random_function(f[1],x, y)*evaluate_random_function(f[2],x, y)
        if f[0] == "avg":
            return (evaluate_random_function(f[1],x, y)+evaluate_random_function(f[2],x, y))/2.
        if f[0] == "square":
            return evaluate_random_function(f[1],x, y)**2
                    
                        
    # your code goes here

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        returns the output value in output range 
    """
    ratio =(val - input_interval_start)/(input_interval_end-input_interval_start)
    return (ratio*(output_interval_end - output_interval_start) + output_interval_start)

im = Image.new("RGB",(350,350))         # creating a new image with the size 350 by 350
red = build_random_function(2,3)        # create function for each color
green = build_random_function(5,6)
blue = build_random_function(3,4)
pixels = im.load()                      # load the pixels


for i in range(350):
    for j in range(350):
        x = remap_interval(i, 0, 350, -1, 1)        # turning pixel location into [-1, 1]
        y = remap_interval(j, 0, 350, -1, 1)        
        r1 = evaluate_random_function(red, x,y)     # values for each color using the function generated for each color
        g1 = evaluate_random_function(green, x,y)
        b1 = evaluate_random_function(blue, x,y)
        r = remap_interval(r1, -1, 1, 0, 255)       # change it to (0,255), the color scale
        g = remap_interval(g1, -1, 1, 0, 255)
        b = remap_interval(b1, -1, 1, 0, 255)
        pixels[i,j] = (int(r), int(g), int(b))      # plotting with the scale 
im.save("img4.JPEG")                                # save the as the JPEG file