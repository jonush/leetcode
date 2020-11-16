"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""

def maximum69Number(num: int) -> int:
    """
    Given an integer containing only 6's and 9's:
    
    - change one digit to get the biggest integer possible. 
    - to get biggest integer, 9's should be on the left
    - will never change a 9 to a 6
    """

    # turn integer into a str then a list
    max_num = list(str(num))

    # if num is already the highest value possible, return num
    if "6" not in max_num:
        return num

    # iterate over list and changee the first 6 into a 9
    for i, n in enumerate(max_num):
        if n is "6":
            max_num[i] = "9"
            # change back into one str and then into integer
            return int("".join(max_num))

maximum69Number(6666)
maximum69Number(9669)
maximum69Number(9969)
maximum69Number(9996)