"""
MEDIUM

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""

def countSubstrings(s: str) -> int:
    ans = 0

    for i in range(len(s) * 2 - 1):
        l = i // 2
        r = l + i % 2
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ans += 1
            l -= 1
            r += 1
    
    return ans