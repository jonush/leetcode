"""
Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.
"""

def find_pair(nums, S):
    # create dictionary for all key/value pairs adding up  to sum S
    d = {}

    # adding in the key/value pairs
    for n in nums:
        # if num not in dictionary
        if n not in d:
            d[n] = 0

    # assign other integer of the pair as the value
    for k, v in d.items():
        if S - k in nums:
            d[k] = S - k

    # list for preparing return type
    new_list = []

    # select valid pairs from the dictionary
    for k, v in d.items():
        temp = []
        if d[k] is not 0:
            temp.append(k)
            temp.append(d[k])
            temp.sort()
            new_list.append(temp)

    # use set and list comprehension to remove duplicate pairs
    num_set = set(tuple(n) for n in new_list)
    ans = [ list(n) for n in num_set ]

    print(ans)

    return ans

num_list = [3, 5, 2, -4, 8, 11]
sum_value = 7

find_pair(num_list, sum_value)