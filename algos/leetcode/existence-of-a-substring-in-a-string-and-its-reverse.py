#https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        items = {}
        for i in range(0,len(s)-1):
            items[s[i:i+2]] = {}
        for i in range(0,len(s)-1):
            if s[i:i+2][1] + s[i:i+2][0] in items:
                return True
        return False