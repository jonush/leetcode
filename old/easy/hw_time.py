"""
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

EXAMPLE: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4 -> RETURNS 1

Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.
"""

def busyStudent(startTime, endTime, queryTime: int) -> int:
    """
    Count the number of students that are doing homework during the given queryTime,
    between two intervals: startTime and endTime.
    """
    
    # counter for number of students doing homework
    doing_hw = 0
    
    # loop through the length of the given list
    # the startTime and endTime will be the same length
    for i in range(0, len(startTime)):
        # if the queryTime is found between the range where a student is doing homework
        if queryTime in range(startTime[i], endTime[i] + 1):
            # increment the counter
            doing_hw += 1
                
    return doing_hw

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
busyStudent(startTime, endTime, queryTime)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

The for loop iterates from a range of O to the len of the provided input list, making that O(n) where n is the length of the input. The search for queryTime in the range of the two input lists happens in O(1) in Python 3, but would have bene O(n) in Python 2.

SPACE: O(1)

The solution does not utilize any additional data structures to find the answer, and searches thorugh the given input instead. A variable is used to store the number of students doing homework, which takes up O(1) space.

"""