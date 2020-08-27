"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

def longestPalindrome(self, s: str) -> str:
    sub = ""
    
    for i in range(len(s)):
        sp = self.check_p(s, i, i)
        if len(sp) > len(sub):
            sub = sp
            
        sp = self.check_p(s, i, i + 1)
        if len(sp) > len(sub):
            sub = sp
        
    return sub

def check_p(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        
    return s[l+1:r]