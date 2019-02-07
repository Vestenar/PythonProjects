def boxBlur(image):
    row, col = len(image), len(image[0])  # row rows, col columns
    ans = []
    for i in range(1, row-1):
        ans.append([])
        for j in range(1, col-1):
            flsum = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    flsum += image[i+k][j+l]
            ans[i-1].append(int(flsum/9))

    return ans


'''
The pixels in the input image are represented as integers. 
The algorithm distorts the input image in the following way: 
Every pixel x in the output image has a value equal to the average value 
of the pixel values from the 3 × 3 square that has its center at x, including x itself.
All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]

the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: 
(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. 
The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]

the output should be

boxBlur(image) = [[5, 4], 
                  [4, 4]]
'''