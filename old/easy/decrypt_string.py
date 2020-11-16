import string

"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
"""

def freqAlphabets(s: str) -> str:
    """
    Given a string "s", map the integers from 1 - 26# to the alphabet:
    - 1 to 9 
    - 10# to 26#
    - return the converted letters as a single string
    """
    
    # split the alphabet into two halves (1 to 9) (10 to 26)
    a_to_i = list(string.ascii_lowercase)[:9]
    j_to_z = list(string.ascii_lowercase)[9:]
    
    # create dictionaries to map the integers to letters
    d1 = {}
    d2 = {} 
    
    # map the integers to the letter dictionaries
    for i, letter in enumerate(a_to_i):
        if i + 1 not in d1:
            d1[str(i + 1)] = letter
            
    for i, letter in enumerate(j_to_z):
        if i + 10 not in d2:
            d2[str(i + 10) + "#"] = letter
            
    # combine the two dictionaries
    d1.update(d2)
    
    chars = []
    reverse = list(s[::-1])
    
    # split the string into letters for iterating through with d1
    for i, l in enumerate(reverse):
        if l is not "#":
            chars.append(l)
        else:
            temp = ""
            temp += reverse[i + 2] + reverse[i + 1] + reverse[i]
            chars.append(temp)
            del reverse[i:i + 2]
            
    chars = chars[::-1]
    
    ans = ""

    for i in chars:
        ans += d1[i]
        
    return ans

test = "10#11#12"
freqAlphabets(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n²)

The two for loops used to create the dictionaries are each O(n). When cleaning up the given string "s", the for loop is O(n), but also consists of a del method which in itself is also O(n). This makes the runtime O(n²). Since the append method adding to the end of the list, that is  O(1) operation, otherwise the overall runtime would go up to O(n³).

SPACE: O(n)

The solution utilizes dictionaries and lists to store the alphabet as well as the cleaned string "s". At the most, each of these will only go up to the length n of the given string "s". The alphabet characters stored in the dictionaries will go up to 26 letters at most. 
"""