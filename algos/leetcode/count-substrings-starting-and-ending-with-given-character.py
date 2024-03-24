#https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

class Solution:
    def optimMe(self, sToOptim):
        if len(sToOptim) == 0:
            return sToOptim[0], 1
        firstChar = sToOptim[0]
        for i, c in enumerate(sToOptim[1:]):
            if c != firstChar:
                return sToOptim[:i+1], 1+i
        return sToOptim, len(sToOptim)   
            
    def countSubstrings(self, s: str, c: str) -> int:
        numberOfMatches = 0
        i = 0
        while i < len(s):
            char = s[i]

            if char == c:
                chaine, longueur = self.optimMe(s[i:])
                nu = 1
                if longueur > 1:     #if characters are in a row we can optimize
                    nu = longueur
                    i = i + longueur - 1
                    numberOfMatches += longueur * (longueur+1)/2  #combinations of n characters 
                    i+=1
                for charBis in s[i:]:
                    if charBis == c:
                        numberOfMatches +=nu
            i+=1
        return int(numberOfMatches)
