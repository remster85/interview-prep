#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Handle edge case for empty or single-element array
        if not nums:
            return None  # or raise an exception as needed
        if len(nums) == 1:
            return nums[0]

        while left < right:
            m = (left + right) // 2
            print(f"Left: {left}, Right: {right}, Middle: {m}, nums[m]: {nums[m]}")

            # Check if the middle element is the minimum
            if m > 0 and nums[m] < nums[m - 1]:  # Check if current middle is the minimum
                return nums[m]
            if m < len(nums) - 1 and nums[m + 1] < nums[m]:  # Check if the next element is the minimum
                return nums[m + 1]

            # Decide which side to continue searching
            if nums[m] >= nums[right]:  # If middle element is greater than the rightmost element
                left = m + 1  # Minimum must be in the right half
            else:  # If middle element is less than the rightmost element
                right = m  # Minimum is in the left half (including middle)

        # At the end of the loop, left should point to the minimum element
        return nums[left]  # Return the minimum element
    

# import random

# # Generate a very long array (length of 10,000) which is rotated sorted
# def generate_rotated_sorted_array(length: int) -> List[int]:
#     # Generate a sorted array of unique integers
#     sorted_array = sorted(random.sample(range(1, 100001), length))
    
#     # Determine the rotation point
#     rotation_point = random.randint(1, length - 1)
    
#     # Rotate the array
#     rotated_array = sorted_array[rotation_point:] + sorted_array[:rotation_point]
    
#     return rotated_array

# # Generate a long rotated sorted array
# long_rotated_array = generate_rotated_sorted_array(10000)


# nums=long_rotated_array
# print(long_rotated_array)
# print(min(long_rotated_array))
# print(Solution().findMin(nums))
