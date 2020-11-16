"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

def isValid(s: str) -> bool:
    """
    Given a string of parentheses:
    - return true if the parentheses close properly
    - false if they do not
    
    - any valid string should have an even length
    """
    
    # if len(s) is odd, doesn't work
    if len(s) % 2 != 0:
        return False
    
    
    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    stack = []
    
    for paren in s:
        # add the opening parentheses to the stack
        if paren in opening:
            stack.append(paren)
        else:
            # if starting with a closed parentheses, return False
            if len(stack)==0:
                return False
            # pop the parenthese in the stack to check validity
            last_open = stack.pop()
            # if parentheses matches in not set, it isn't valid
            if (last_open, paren) not in matches:
                return False
    
    return len(stack)==0

test = "(){}[]"
isValid(test)

"""
TIME & SPACE COMPLEXITY

TIME: 

SPACE: 
"""