"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target: int):
    """
    Given a list of numbers and a target sum,
    return the indices of two numbers who add
    up to the desired target sum.
    """

    d = {}
    
    for i, n in enumerate(nums):
        m = target - n
        
        if m in d:
            return [d[m], i]
        else:
            d[n] = i
  
test = [1,5,2,9]
test_target = 7
twoSum(test, test_target)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

The solution utilizes a dictionary to check the list of nums. The for loop used to iterate through the list has a runtime of O(n), with n being the length of the input parameter.

SPACE: O(n)

The solution utilizes a dictionary to store the numbers and their indices. In the worst case, where the second number of the sum is the last item in nums, the dictionary will have been created with a size of N - 1. If the second number is found before the end, the dictionary will end as the result is returned.
"""

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(6))