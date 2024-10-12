# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:

    def isStrictPalindrome(self, s: str) -> bool:
        print("checking isStrictPalindrome " + s)
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        deletions = 0
    
        while i < j  and deletions < 2:
            if s[i] != s[j]:
                if deletions == 1:
                    return False
                if  s[i+1] == s[j] and s[i] == s[j-1]:
                    t1 = self.isStrictPalindrome(s[i:j])
                    t2 = self.isStrictPalindrome(s[i+1:j+1])
                    return t1 or t2
                elif s[i+1] == s[j]:
                    i+=1
                elif s[i] == s[j-1]:
                    j-=1 
                else:
                    return False
                deletions += 1
            else:    
                i+=1
                j-=1
        return deletions < 2


#or

class Solution:

    def isStrictPalindrome(self, s: str) -> bool:
        print("checking isStrictPalindrome " + s)
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        deletions = 0
    
        while i < j  and deletions < 2:
            if s[i] != s[j]:
                if deletions == 1:
                    return False
                if  s[i+1] == s[j] and s[i] == s[j-1]:
                    t1 = self.isStrictPalindrome(s[i:j])
                    t2 = self.isStrictPalindrome(s[i+1:j+1])
                    return t1 or t2
                elif s[i+1] == s[j]:
                    return self.isStrictPalindrome(s[i+1:j+1])
                elif s[i] == s[j-1]:
                    return self.isStrictPalindrome(s[i:j])
                else:
                    return False
            i+=1
            j-=1
        return True
