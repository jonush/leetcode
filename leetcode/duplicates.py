def containsDuplicate(nums):
    """
    # solution using a dictionary
    # use a dictionary to log all numbers
    d= {}
    
    for i in nums:
        if i not in d:
            d[i] = 0
        # if a number is already in the dictionary, increment count by 1
        d[i] += 1
    
    # if any number has a count greater than 1, return True
    for count in d.values():
        if count > 1:
            return True
    # else, return False
    return False
    """
    
    # solution using sets
    if len(set(nums)) < len(nums):
        return True
    else:
        return False

test = [1,1,1,3,3,4,3,2,4,2]

containsDuplicate(test)