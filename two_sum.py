def twoSum(nums, target):
    # create a dictionary for each number
    d = {}
    index = 0
    ans = []
    
    # store index of each number as a dictionary value
    for n in nums:
        if n not in d:
            d[n] = []
        d[n].append(index)
        index += 1
        
    print(d)
    
    # subtract a number from the target to locate the second number
    for n in d.keys():
        if target - n in d.keys():
            # if target == 2n:
            if target - n == n:
                # if n shows up more than once:
                if len(d[n]) > 1:
                    target -= n
                    # get the index of the first number
                    ans.append(d[n].pop(0))
                    break
                else:
                    continue
            else:
                target -= n
                # get the index of the first number
                ans.append(d[n].pop(0))
                break
        
    if target in d.keys():
        # get the index where the subtracted number appears
        ans += d[target]
            
    # return both indices as a list
    return ans