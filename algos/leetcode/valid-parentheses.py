#https://leetcode.com/problems/valid-parentheses/
class Solution:
    
    
    def isValid(self, s: str) -> bool:
        
        currentStreak = ''
        left = {}
        right = {}
        
        left['('] = 0
        right['('] = 0
        left['{'] = 0
        right['{'] = 0
        left['['] = 0
        right['['] = 0
        
        parenthesesMap = {}
        parenthesesMap['('] = ')'
        parenthesesMap['{'] = '}'
        parenthesesMap['['] = ']'
        parenthesesMap[')'] = '('
        parenthesesMap['}'] = '{'
        parenthesesMap[']'] = '['
        
        for c in s:
            
            if c in ['(','{','[']:
                left[c] +=1
                ch = c
                currentStreak = ch
            else:
                right[parenthesesMap[c]] +=1
                ch = parenthesesMap[c]
                if currentStreak != '' and ch != currentStreak:
                    print(f"current streak {currentStreak} {ch} is broken")
                    return False
                currentStreak = ch
                
            
            if right[ch] > left[ch]:
                return False
            
        return left['('] == right['('] and left['{'] == right['{'] and left['['] == right['['] 
        
        
    def isValidStack(self, s: str) -> bool:
        
        parenthesesMap = {}
        parenthesesMap['('] = ')'
        parenthesesMap['{'] = '}'
        parenthesesMap['['] = ']'
        parenthesesMap[')'] = '('
        parenthesesMap['}'] = '{'
        parenthesesMap[']'] = '['
        
        if len(s) == 0:
            return False
        
        if len(s) % 2 == 1:
            return False
        
        if s[0] in [')','}',']']:
            return False
        
        if s[len(s)-1] in ['(','{','[']:
            return False
        
        
        stack = []
        for c in s:    
            if c in ['(','{','[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                cc = stack.pop()
                if cc != parenthesesMap[c]:
                    return False

        return len(stack) == 0
    