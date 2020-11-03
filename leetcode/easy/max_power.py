"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

EX: "leetcode" returns -> 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
"""

def maxPower(s: str) -> int:
    # at the least, each letter is a power of 1
    max_power = power = 1

    # iterate through the string to find the letter with the highest power
    for i in range(len(s) - 1):  
        if s[i + 1] == s[i]:
            power += 1
        else:
            power = 1

        # record the highest power
        if power >= max_power:
            max_power = power
    
    
    return max_power

test = "aaasdddgggeethhhhhaac"
maxPower(test)