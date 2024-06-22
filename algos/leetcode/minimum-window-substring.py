#https://leetcode.com/problems/minimum-window-substring
#HARD
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        charMapReference = Counter(t)
        charMapWindow = Counter()
        
        # Initialize pointers and variables
        left, right = 0, 0
        formed = 0  # Tracks how many characters have formed the desired window
        minLen = float('inf')
        minWindow = ""
        
        while right < len(s):
            # Expand the window by moving the right pointer
            char = s[right]
            charMapWindow[char] += 1
            
            # Check if this character satisfies the requirement
            if char in charMapReference and charMapWindow[char] == charMapReference[char]:
                formed += 1
            
            # Try to contract the window by moving the left pointer
            while formed == len(charMapReference) and left <= right:
                currentLen = right - left + 1
                if currentLen < minLen:
                    minLen = currentLen
                    minWindow = s[left:right+1]
                
                # Contract the window from the left
                charLeft = s[left]
                charMapWindow[charLeft] -= 1
                if charMapWindow[charLeft] < charMapReference[charLeft]:
                    formed -= 1
                left += 1
            
            # Move right pointer to expand the window further
            right += 1
        
        return minWindow
