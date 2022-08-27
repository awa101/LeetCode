class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s, i, i)  # odd case, like "aba"
            if len(tmp) > len(res):
                res = tmp
            
            tmp = self.helper(s, i, i+1) # even case, like "abba"
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]