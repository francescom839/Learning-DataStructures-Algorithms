"""
This is my solution to the 6th problem of the week 4 of the "Data Structure and Algorithm Specialization" offered by the University of California San Diego. 
- - - Organizing a Lottery - - -
Given a set of points and a set of segments on a line, compute, for each point, the number of segments it is contained in.
Input: A list of segments and a list of points.
Output: The number of segments containing each point.
"""
from sys import stdin


def count_segments(starts, ends, points):
    countDict = {}
    segments_num = 0
    
    # Create a list of tuples with left values, winning points and right values
    listpoints = [(x, 'l') for x in starts]
    listpoints += [(x, 'p') for x in points]
    listpoints += [(x, 'r') for x in ends]

    listpoints.sort() # Sort all the segments and the points

    for p in listpoints:
        if p[1] == 'l':
            segments_num += 1 # Counts how many segments have started
        elif p[1] == 'r':
            segments_num -= 1
        else: # When we reach a winning point, save the current value with the amount of segments containing it
            countDict[p[0]] = segments_num # adds the current value of segments_num to the dictionary cnt with the point as the key.

    return [countDict[x] for x in points] # return a list of counts


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = count_segments(input_starts, input_ends, input_points)
    print(*output_count)
