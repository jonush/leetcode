def containsDuplicate(nums):
    
    # solution using sets
    if len(set(nums)) < len(nums):
        return True
    else:
        return False

test = [1,1,1,3,3,4,3,2,4,2]

containsDuplicate(test)