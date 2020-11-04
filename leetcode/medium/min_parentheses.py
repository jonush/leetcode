"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

- It is the empty string
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
"""

def minAddToMakeValid(S: str) -> int:
    """
    Return the minimum number of parentheses that need to be
    added to balance out the parentheses string "S"
    
    The string is considered balanced if:
    - the string is empty
    - AB where A + B
    - (A)
    """
    
    open_p = close_p = 0
    
    for i in S:
        # if close_p is already 0, increment open_p
        if close_p is 0 and i == ")":
            open_p += 1
        else:
            # if i is "(", increment close_p
            if i == "(":
                close_p += 1
            # if i is ")", decrement close_p
            else:
                close_p -= 1
    
    return open_p + close_p

test = "()))(("
minAddToMakeValid(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

The solution uses a for loop to iterate over the string once, so the n depends on the size of the input string.

SPACE: O(1)

THe solution does not require any additional data structures, using only two variables to track the minimum number of parentheses required to balance the string.

"""