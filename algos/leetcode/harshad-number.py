#https://leetcode.com/problems/harshad-number 
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        sum = 0
        for c in str(x):
            sum += int(c)
        fraction = x / sum
        return -1 if fraction - int(fraction) != 0 else sum
        