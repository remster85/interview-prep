#https://leetcode.com/problems/letter-combinations-of-a-phone-number/ 
class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        digitMaps = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        def buildCombination(current, index):

            if index == len(digits):
                result.append("".join(current))
                return

            for char in digitMaps[digits[index]]:
                current.append(char)
                buildCombination(current ,index + 1)
                current.pop()

        result = []
        buildCombination([], 0)
        return result







        