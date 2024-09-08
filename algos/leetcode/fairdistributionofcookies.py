#https://leetcode.com/problems/fair-distribution-of-cookies/?envType=problem-list-v2&envId=backtracking
import itertools

from itertools import combinations

class Solution:

    def generate_partitions(self, arr, k):
        def backtrack(start, partitions):
            # If we've assigned all elements and have k non-empty lists
            if start == len(arr) and len([p for p in partitions if p]):
                if len([p for p in partitions if p]) == k:
                    result.append([p.copy() for p in partitions])
                return
            
            # Try assigning the current element to each partition
            for i in range(k):
                partitions[i].append(arr[start])
                backtrack(start + 1, partitions)
                partitions[i].pop()
                # If a partition is empty, don't assign to further partitions to avoid duplicates
                if not partitions[i]:
                    break
        
        result = []
        partitions = [[] for _ in range(k)]
        backtrack(0, partitions)
        return result

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res = self.generate_partitions(cookies, k)
        #print(len(res))
        minUnfairness = 999999999999
        print(res)
        max_sums = []

        # Iterate through each group of sublists
        for group in res:
            # Calculate the sum of each sublist in the group
            sublist_sums = [sum(sublist) for sublist in group]
            # Find the maximum sum in the current group
            max_sum = max(sublist_sums)
            # Append the maximum sum to the list of max_sums
            max_sums.append(max_sum)

        return  min(max_sums)