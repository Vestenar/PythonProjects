import math
# def rectangleRotation(a, b):
#     pt = 0
#     radius = pow(a / 2, 2) + pow(b / 2, 2)
#     radius = int(math.ceil(pow(radius, .5)))
#
#     for i in range(-radius, radius + 1):
#         for j in range(-radius, radius + 1):
#             x = i * math.cos(math.radians(-45)) - j * math.sin(math.radians(-45))
#             y = i * math.sin(math.radians(-45)) + j * math.cos(math.radians(-45))
#             if -a / 2 <= x <= a / 2 and -b / 2 <= y <= b / 2:
#                 pt += 1
#
#     return pt

def rectangleRotation(a, b):
    [m, n] = [int(math.floor(x / math.sqrt(2))) for x in (a, b)]
    return m * n + (m + 1) * (n + 1) - (m + n) % 2
print(rectangleRotation(30,2))
'''
A rectangle with sides equal to even integers a and b is drawn 
on the Cartesian plane. Its center (the intersection point of its diagonals) 
coincides with the point (0, 0), but the sides of the rectangle 
are not parallel to the axes; instead, they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?

Example

For a = 6 and b = 4, the output should be
rectangleRotation(a, b) = 23.

The following picture illustrates the example, and the 23 points are marked green.
'''
