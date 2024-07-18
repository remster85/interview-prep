#https://leetcode.com/problems/find-all-anagrams-in-a-string
from collections import Counter
import copy

class Solution:


    def findAnagrams(self, s: str, p: str) -> List[int]:

        i = 0
        window = len(p)
        pSorted = ''.join(sorted(p))
        output = []

        for i in range(0, len(s)-window+1):
            ww  = ''.join(sorted(s[i:window+i]))
            if pSorted == ww:
                output.append(i)
        return output