def runnersMeetings(startPosition, speed):
    n = [-1]
    time = 0
    while True:
        distance = [0 for i in range(len(speed))]
        for i in range(len(speed)):
            distance[i] = speed[i]/60 * time + startPosition[i]
        if len(distance) != len(set(distance)):
            n.append(1+len(distance) - len(set(distance)))
        time +=1
        if time > 60:
            break
    return max(n)


start = [1, 4, 2]
speed = [27, 18, 24]
print(runnersMeetings(start, speed))

'''
Some people run along a straight line in the same direction. 
They start simultaneously at pairwise distinct positions and run with constant speed 
(which may differ from person to person).

If two or more people are at the same point at some moment we call that a meeting. 
The number of people gathered at the same point is called meeting cardinality.

For the given starting positions and speeds of runners find the maximum meeting 
cardinality assuming that people run infinitely long. If there will be no meetings, return -1 instead.

Example

For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
runnersMeetings(startPosition, speed) = 3.

In 20 seconds after the runners start running, 
they end up at the same point. 
'''