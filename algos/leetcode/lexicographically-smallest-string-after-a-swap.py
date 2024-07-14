#https://leetcode.com/contest/weekly-contest-406/problems/lexicographically-smallest-string-after-a-swap/
class Solution:
    def getSmallestString(self, s: str) -> str:
        output = ""
        for i, c in enumerate(s):
            if i >=1 and int(c) % 2 == int(s[i-1]) % 2 and int(c) < int(s[i-1]):
                output = output[0:len(output)-2+1] + c + s[i-1]
                return output + s[i+1: len(s)]
            else:
                output +=  c
        return output