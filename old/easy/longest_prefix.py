"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs) -> str:
    """
    given a list of strings:
    - return the longest common prefix of all strings
    - if none found, return ""
    """
    
    # check if strs is empty
    if not strs:
        return ""
    
    # get the shortest word in strs
    shortest = min(strs,key=len)
    
    # iterate through the shortest word
    for i, ch in enumerate(shortest):
        # iterate through the list of strings
        for other in strs:
            # if the character does not match
            if other[i] != ch:
                # return all characters up to index i in shortest
                return shortest[:i]
    
    # if all characters in shortest match, return shortest
    return shortest

test = ["flow", "flower", "fleet"]
longestCommonPrefix(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n²)

The solution utilizes a double for loop to iterate over the shortest word, and the rest of the strings, leading to a O(n²) runtime complexity.

SPACE: O(1)

The solution uses a "shortest" variable to store the shortest word in strs.
"""