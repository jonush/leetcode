"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.
"""

def findMin(nums) -> int:
    """
    Given an array of ascending sorted integers,
    return the minimum number after 'n' rotations
    """
    # determine the start and end 
    left, right = 0, len(nums)-1
    
    while left < right:
        # find the mid index
        mid = (left + right) // 2
        
        # find the mid value to locate rotation range
        if nums[mid] > nums[right]:
            # highest value is in right side of range
            left = mid + 1
        else:
            # highest value is in left side of range
            right = mid
            
    return nums[left]

test = [3,4,5,1,2]
findMin(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(nlog(n))

The solution utilizes a while loop for a O(n) operation. The traversal over the left, right, and mid values is an O(log(n)) operation, with the number of values traversed decreasing over time. At most, the traversal my be O(n) if all values need to be traversed to determine the minimum.

SPACE: O(1)

The slution does not use any additional data structures, so it does not take up any additional space outside of the given input array.
"""