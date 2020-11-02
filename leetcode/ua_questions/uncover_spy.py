def uncover_spy(n, trust):
    """
    TRY TO OPTIMIZE SOLUTION -> REFACTOR CODE
    :type n: integer
    :type trust: list
    :rtype: integer
    """

    d = {}
    
    counter = 0
    
    # iterating over trust array -> O(n)
    # add all numbers that trust someone into the keys
    # if someone is trusted, add them to the values list of who is trusting them
    for i in trust:
        if i[0] not in d:
            d[i[0]] = set()
        d[i[0]].add(i[1])    # O(1)
    
    print(d)

    # locating the spy -> whoever doesn't trust anyone & is trusted by everyone else
    # iterating over trust array -> O(n)    
    for i in trust:
        if i[1] not in d.keys():
            if i[1] in d[i[0]]:
                counter += 1
    
    # iterating over trust array -> O(n)
    for i in trust:
        if i[1] not in d.keys() and counter == n - 1:
            return i[1]
        else:
            return -1

test = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]

print(uncover_spy(4, test))