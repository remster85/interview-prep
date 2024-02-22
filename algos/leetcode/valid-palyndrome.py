#https://leetcode.com/problems/valid-palindrome/
class Solution:

    def isEligibleChar(self, c: chr) -> bool:
        v = ord(c)
        if (v >= ord('A') and v <= ord('Z')) or (v >= ord('0') and v <= ord('9')):
            return True
        return False 

    def isPalindrome(self, s: str) -> bool:
        cleanS = [x for x in s.upper() if self.isEligibleChar(x)]
        for i in range(0, len(cleanS)):
            if cleanS[i] != cleanS[len(cleanS)-i-1]:
                return False
        return True
        