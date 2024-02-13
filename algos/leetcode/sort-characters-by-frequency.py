#https://leetcode.com/problems/sort-characters-by-frequency/

import heapq 

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        heap = []

        dic = {}

        for c in s:
            dic[c] = dic.get(c, 0) + 1

        max_heap = [(-freq, char) for char, freq in dic.items()]
        heapq.heapify(max_heap)
        
        # Build the result string
        result = ""
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result += char * (-freq)
        
        return result