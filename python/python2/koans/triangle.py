#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    side = sorted([a, b, c])

    if 0 in side:
        raise TriangleError, "Side length cannot be 0"
    elif side[0] < 0:
        raise TriangleError, "Side length cannot be below 0"
    elif side[0] + side[1] < side[2]:
        raise TriangleError, "Incoherent side lengths"

    types = {
        1: 'equilateral',
        2: 'isosceles',
        3: 'scalene'
    }
    side_length_count = len(set(side))
    return types[side_length_count]


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
