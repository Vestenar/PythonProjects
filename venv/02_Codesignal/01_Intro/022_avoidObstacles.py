def avoidObstacles(inputArray):
    jump = 1
    a = 0
    while a < max(inputArray)//jump:
        jump += 1
        for i in range(1, max(inputArray)//jump+1):
            if jump*i not in inputArray:
                a += 1
            else:
                a = 0
                break

    return jump


'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. 
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.'''