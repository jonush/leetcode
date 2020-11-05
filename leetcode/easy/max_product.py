"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

EXAMPLE: nums = [3,4,5,2] -> RETURNS 12

Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
"""

def maxProduct(nums) -> int:
    """
    Find the maximum product of two numbers in `nums`,
    where the numbers are (nums[i] - 1) and (nums[j] - 1)
    
    - find the max product of the two largest integers in nums
    - subtract one from each integer and return the product
    """
    
    # find the first largest num
    max_one = max(nums)
    # remove it from the nums list
    nums.remove(max_one)
    # find the next largest number
    max_two = max(nums)
    
    # return the product
    return (max_one - 1) * (max_two - 1)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

While there are no for loops in the solution, using the max() method is O(n) since it requires iterating through the input of length n to find the largest integer. It does this twice, once for each max_value so the overall general runtime complexity is O(n). The remove() method is also an O(n) operation since it requires iterating through the input list to find the first occurrence of the selected integer.

SPACE: O(1)

The solution utilizes variables to store the max values, but no additional data structures. It does remove a value from the original input list.
"""