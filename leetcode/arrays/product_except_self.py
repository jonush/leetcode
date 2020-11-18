"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

def productExceptSelf(nums):
    """
    Given a list of numbers,
    return a new list where each item is the product
    of all numbers excep the one at that index in nums
    
    - the nums list will always have more than one number
    """
    
    # the position incrementer
    p = 1
    n = len(nums)
    output = []
    
    # from left to right, initialize the output list
    # with each number being a product of the numbers before it
    for i in range(0, n):
        output.append(p)
        p *= nums[i]
        
    # reset the position incrementer
    p = 1
    # repeat the iteration from right to left
    for i in range(n-1, -1, -1):
        output[i] *= p
        p *= nums[i]
        
    return output

test = [1,3,5,2,6]
productExceptSelf(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

The solution will iterate over the list of nums in two separate for loops, making the runtime O(2n), which can be generalized to an overall runtime of O(n).

SPACE: O(1)

Not counting the additional space for the returned output array, the solution does not utilize any additional data structures.
"""