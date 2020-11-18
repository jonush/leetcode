def maxSubArray(nums) -> int:
  """
  Given a list of numbers, find the largest sum out of a contiguous subarray
  
  When should the subarray window move forward?
      • take sum of array from [i:]
      • save that value
      • take sum of array from [i:j] where j approaches the left
  """
  
  for i in range(1, len(nums)):
      if nums[i-1] > 0:
          nums[i] += nums[i-1]
          
  return max(nums)

test = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

The solution iterates over the list of numbers for an O(n) runtime.

SPACE: O(1)

The solution does not utilize any additional data structures.
"""