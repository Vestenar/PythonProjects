def drawRectangle(canvas, rectangle):
    a0 = rectangle[0]
    a1 = rectangle[1]
    b0 = rectangle[2]
    b1 = rectangle[3]
    canvas[a1][a0] = "*"
    canvas[b1][b0] = "*"
    canvas[a1][b0] = "*"
    canvas[b1][a0] = "*"
    for i in (a1, b1):
        for j in range(a0+1, b0):
            canvas[i][j] = "-"
    for i in range(a1+1, b1):
        for j in (a0, b0):
            canvas[i][j] = "|"

    for can in canvas:
        print(can)
    return canvas



canvas =    [["a","a","a","a","a","a","a","a"],
             ["a","a","a","a","a","a","a","a"],
             ["a","a","a","a","a","a","a","a"],
             ["b","b","b","b","b","b","b","b"],
             ["b","b","b","b","b","b","b","b"]]

rectangle = [0, 1, 4, 3]

print(drawRectangle(canvas, rectangle))
'''
You are implementing a command-line version of the Paint app. 
Since the command line doesn't support colors, you are using different characters to represent pixels. 
Your current goal is to support rectangle x1 y1 x2 y2 operation, 
which draws a rectangle that has an upper left corner at (x1, y1) 
and a lower right corner at (x2, y2). 
Here the x-axis points from left to right, and the y-axis points from top to bottom.

Given the initial canvas state and the array that represents the coordinates 
of the two corners, return the canvas state after the operation is applied. 
For the details about how rectangles are painted, see the example.

Example

For

canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

and rectangle = [1, 1, 4, 3], the output should be


drawRectangle(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                                    ['a', '*', '-', '-', '*', 'a', 'a', 'a'],
                                    ['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
                                    ['b', '*', '-', '-', '*', 'b', 'b', 'b'],
                                    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]

Note that rectangle sides are depicted as -s and |s, asterisks (*) stand for its corners 
and all of the other "pixels" remain the same. 
Color in the example is used only for illustration.
'''
