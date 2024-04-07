#https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/submissions/ 
#contest 20240407
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        maxIncreasingStreak = 0
        maxDecreasingStreak = 0
        increasingStreak = 1
        decreasingStreak = 1   
        
        for i, element in enumerate(nums):
            print(f"i={i} element={element} ")
            if i>0 and nums[i] > nums[i-1]:
                increasingStreak+=1
            else:
                maxIncreasingStreak = max(increasingStreak,maxIncreasingStreak )
                increasingStreak = 1                
                
            if i>0 and nums[i] < nums[i-1]:
                decreasingStreak+=1     
            else:
                maxDecreasingStreak = max(decreasingStreak,maxDecreasingStreak )
                decreasingStreak = 1
        return max(maxDecreasingStreak, maxIncreasingStreak, decreasingStreak, increasingStreak)
                
        
        
        