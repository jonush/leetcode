"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""

def lengthOfLongestSubstring(s: str) -> int:
    # initialize starting length
    max_length = start = 0
    
    # dictionary for seen characters
    used = {}
    
    for i, c in enumerate(s):
        # if character has been seen after the reset count
        if c in used and start <= used[c]:
            # start search from next new character
            start = used[c] + 1
        # else, return the length
        else:
            max_length = max(max_length, i - start + 1)

        # store new characters in the dictionary
        used[c] = i

    return max_length