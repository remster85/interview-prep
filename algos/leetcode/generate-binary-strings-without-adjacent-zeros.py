#https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros
import itertools

class Solution:
    
    def foo(self, l, n):
        yield from itertools.product(*([l] * n)) 
        
    def validStrings(self, n: int) -> List[str]:
        output = []
        for combination in self.foo('01', n):
            tentative = ''.join(combination)
            if '00' not in tentative:
                output.append(tentative)
        return output