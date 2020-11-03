"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

EXAMPLE: [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]] -> "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
"""

def destCity(paths) -> str:
    """
    Given a list of [pairs], find the item at index 1 of a pair that is not in any index 0
    - shows up in index 1
    - never at index 0
    """
    
    # use a dictionary to track each item and where it points to
    d = {}
    
    # map the list to the dictionary
    for i in paths:
        # add the origin point to the dictionary keys
        if i[0] not in d:
            d[i[0]] = set()
        # add the linked destination to the values as a set
        d[i[0]].add(i[1])
    
    # find the item that doesn't point anywhere
    for i in d.values():
        ans = i.pop()
        if ans not in d.keys():
            return ans

test = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
destCity(test)