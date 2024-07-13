#https://leetcode.com/problems/find-the-encrypted-string
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        shift = k % len(s)
        return s if shift == 0 else s[shift:] + s[0:shift]

        