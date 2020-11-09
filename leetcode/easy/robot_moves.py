"""
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
"""
def judgeCircle(moves: str) -> bool:
    """
    Given a string of moves ("URDL"),
    determine if a robot returns to the origin (0,0)
    
    - the robot starts from (0,0)
    - U/R moves robot +1
    - D/L moves robot -1
    """
    
    # create a dictionary to store the moves
    d = {
        "U": 1,
        "R": 1,
        "D": -1,
        "L": -1
    }
    
    # counter to track placement on 
    x = y = 0
    
    # iterate through string of moves to track robot placement
    for i in moves:
        if i is "L" or i is "R":
            x += d[i]
        elif i is "U" or i is "D":
            y += d[i]
            
    # check if robot returns to origin
    if x is 0 and y is 0:
        return True
    else:
        return False

test = "UUDLR"
judgeCircle(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

The solution utilizes a for loop to iterate over the moves string to determine where the robot is on the 2D plane, which depends on the length of the input string.

SPACE: O(1)

The solution does utilize a dictionary for the four possible moves, as well as two variables to store the counter for where the robot is. However, no other major data structures are used in the solution.
"""