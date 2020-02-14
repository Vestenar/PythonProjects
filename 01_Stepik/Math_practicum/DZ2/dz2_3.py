from math import sin, cos, atan, pi

def derivative(f, x0=0.):
    dx = 1e-5
    return round((f(x0 + dx) - f(x0)) / dx, 3)


print(derivative(sin, 0))
print(sin(0))
print(derivative(sin, pi/4))
print(derivative(cos, 0))
print(cos(0))
print(derivative(atan, 0))
print(atan(0))
