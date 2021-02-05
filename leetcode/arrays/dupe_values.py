def findDuplicates(nums):
    d = {}
    ans = []
    
    for n in nums:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    
    for k, v in d.items():
        if v is 2:
            ans.append(k)
            
    print(ans)
    return ans

test = [4,3,2,6,8,4,3,2]
findDuplicates(test)