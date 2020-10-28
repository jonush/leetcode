"""
-------EASY-------

On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.

example: [[1,1],[3,4],[-1,0]]
[1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]

"""

def minTimeToVisitAllPoints(points):
    # possible moves:
    # move vertically   ->   p[a+/-1, b]
    # move horizontally ->   p[a, b+/-1]
    # move diagonally   ->   p[a+/-1, b+/-1]   ->   fastest



    # counter for number of steps:
    counter = 0

    for p in range(len(points) - 1):
        # calculate distance between current point and next point
        a, b = abs(points[p+1][0] - points[p][0]), abs(points[p+1][1] - points[p][1])

        counter += max(a, b)

    print(counter)
    return counter

example = [[1,1],[3,4],[-1,0]]

minTimeToVisitAllPoints(example)