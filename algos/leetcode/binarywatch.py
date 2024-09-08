#https://leetcode.com/problems/binary-watch/?envType=problem-list-v2&envId=backtracking

class Solution:

    def readBinaryWatch(self, turnedOn):
        result = []
        
        # Precompute the number of 1s in the binary representation of numbers for hours (0-11) and minutes (0-59)
        hours = [h for h in range(12) if bin(h).count('1') <= turnedOn]
        minutes = [m for m in range(60) if bin(m).count('1') <= turnedOn]
        
        # Iterate over precomputed valid hours and minutes
        for h in hours:
            for m in minutes:
                # If the total number of 1s matches turnedOn, add the time to the result
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append(f"{h}:{m:02d}")
        
        return result

        