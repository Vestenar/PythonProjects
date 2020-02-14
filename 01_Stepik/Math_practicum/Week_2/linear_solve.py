import numpy

def dual():
    a11, a12, b1 = map(float, input().split())
    a21, a22, b2 = map(float, input().split())
    M1 = numpy.array([[a11, a12], [a21, a22]])
    v1 = numpy.array([b1, b2])
    if numpy.linalg.det(M1):
        r = numpy.linalg.solve(M1, v1)
        print(r[0], r[1])
    else:
        print('Система не имеет решений')


def triple():
    a11, a12, a13, b1 = map(float, input().split())
    a21, a22, a23, b2 = map(float, input().split())
    a31, a32, a33, b3 = map(float, input().split())

    M1 = numpy.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
    v1 = numpy.array([b1, b2, b3])
    if numpy.linalg.det(M1):
        r = numpy.linalg.solve(M1, v1)
        print(*r)
    else:
        print('Система не имеет решений')

def quatro():
    lines = [list(map(float, input().split())) for _ in range(4)]
    M1 = numpy.array([line[:-1] for line in lines])
    v1 = numpy.array([line[-1] for line in lines])
    if numpy.linalg.det(M1):
        r = numpy.linalg.solve(M1, v1)
        print(*r)
    else:
        print('Система не имеет решений')

def univ():
    lines = [list(map(float, input().split())) for _ in range(int(input()))]
    M1 = numpy.array([line[:-1] for line in lines])
    v1 = numpy.array([line[-1] for line in lines])
    if numpy.linalg.det(M1):
        r = numpy.linalg.solve(M1, v1)
        print(*r)
    else:
        print('Система не имеет решений')


def classsolve():
    lines = list(map(int, input().split()))
    if lines[0] < lines[1]:
        print('Такой класс не существует')
        return
    M1 = numpy.array([[1, 1], [1, -1]])
    v1 = numpy.array(lines)
    if not numpy.linalg.det(M1):
        print('Такой класс не существует')
    else:
        r = [int(i) for i in numpy.linalg.solve(M1, v1)]
        if r[0] + r[1] == lines[0] and r[0] - r[1] == lines[1]:
            print(*r)
        else:
            print('Такой класс не существует')


def solvegraph():
    n = int(input())
    lines = [list(map(float, input().split())) for _ in range(n)]
    M1 = numpy.array([[line[0]**i for i in range(n)] for line in lines])
    v1 = numpy.array([line[-1] for line in lines])
    if numpy.linalg.det(M1):
        r = numpy.linalg.solve(M1, v1)
        print(*r)
    else:
        print('Система не имеет решений')

solvegraph()