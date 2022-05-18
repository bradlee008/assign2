"""
Bradley Kimutai Kosgei
CS51A
Assignment 2
02/01/2022

For extra credit, I drew the moon

"""

from random import randint
from turtle import *


def triangle(x, y, length):

    """
    draws an equilateral triangle
    :param x: the x coordinate is given
    :param y: the y coordinate is given
    :param length: gives the length of the side of the triangle
    :return: None
    """
    penup()  # lifts the pen up
    goto(x, y)  # moves the turtle to the specific position x, y
    pendown()  # puts the pen down to start drawing
    fillcolor("purple")  # applies color to the stated shape
    begin_fill()  # starts filling the color
    setheading(90)  # rotates the shape by the stated angle

# makes the turtle move forward by a certain length
# then rotates it by an angle 120 three times

    for i in range(3):
        forward(length)
        right(120)
    end_fill()  # stops filling the color


def polygon(x, y, number_of_sides, length):

    """
    draws an n-sided polygon
    :param x: the x coordinate
    :param y: the y coordinate
    :param number_of_sides: gives the number of sides of the polygon
    :param length: length of one side of the polygon
    :return: None
    """

    penup()
    goto(x, y)
    pendown()
    fillcolor("brown")
    begin_fill()
    setheading(0)

# makes the turtle move forward by a certain length
# then rotates it by a certain angle n times

    for i in range(number_of_sides):
        forward(length)
        right(360 / number_of_sides)
    end_fill()


def add_circles(number_of_circles):

    """
    draws randomly placed circles of radius 4
    :param number_of_circles: gives the number of circles
    :return: None
    """
    speed(0)
    for i in range(number_of_circles):
        pu()
        goto(randint(-360, 360), randint(-337, 337))
        pd()
        begin_fill()
        color("white")
        circle(randint(1, 4))  # draw circles of random radii from 1 to 4
        end_fill()


def moon(x, y, number_of_sides, length):

    """

    draws an n-sided polygon
    500 sides creates almost a circle that acts as the moon
    :param x: the x coordinate
    :param y: the y coordinate
    :param number_of_sides: gives the number of sides of the polygon
    :param length: length of one side of the polygon
    :return: None
    """

    penup()
    goto(x, y)
    pendown()
    fillcolor("gray")  # gray color is filled into the moon shape
    begin_fill()
    setheading(0)

# makes the turtle move forward by a certain length
# then rotates it by a certain angle n times

    for i in range(number_of_sides):
        forward(length)
        right(360 / number_of_sides)
    end_fill()


def rectangle(x, y, height, length):

    """
    draws a rectangle and fills it with color depending on the dimensions

    :param x: the x coordinate
    :param y: the y coordinate
    :param height: gives the height of the rectangle
    :param length: gives the length of the rectangle
    :return: None

    """

    penup()
    goto(x, y)
    setheading(180)
    pendown()
    fillcolor()
    begin_fill()

    for i in range(2):
        forward(length)
        right(90)
        forward(height)
        right(90)

    if height == length:  # if the height is equal to length, blue color is applied
        fillcolor("blue")
    elif length > height:  # if the length is greater than the height, red color is applied
        fillcolor("yellow")
    else:
        fillcolor("green")  # if the height is greater than the length, green color is applied
    end_fill()


def generate_picture():

    """
    combines all the functions together to give one final picture

    :return: None
    """
    bgcolor("black")  # gives the background the stated color

    add_circles(130)  # draws 130 randomly placed circles all over the screen each with a random radius

    triangle(-25, 30, 50)  # draws an equilateral triangle at the stated coordinates with the stated length
    triangle(-75, 75, 75)
    triangle(-50, 100, 65)
    triangle(-50, 50, 90)
    triangle(0, 0, 45)
    triangle(-20, 20, 100)

    polygon(70, -250, 8, 79)  # draws an n sided polygon at the stated coordinates
    polygon(150, -250, 7, 75)
    polygon(0, -250, 6, 67)
    polygon(-100, -250, 9, 65)
    polygon(-200, -250, 7, 60)
    polygon(270, 270, 10, 20)

    moon(-275, 275, 750, .8)  # draws a 500 sided polygon that is almost circular to represent the moon
    moon(-245, 245, 100, .5)
    moon(-225, 225, 100, .5)

    rectangle(150, 130, 50, 50)
    rectangle(160, 160, 100, 50)
    rectangle(145, 155, 50, 100)

generate_picture()









