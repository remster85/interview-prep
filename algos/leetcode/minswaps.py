#https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/?envType=company&envId=societe-generale&favoriteSlug=societe-generale-three-months

class Solution:
    def minSwaps(self, s: str) -> int:

        if len(s) ==0 or len(s) ==1:
            return 0

        n0 = s.count('0')
        n1 = len(s) - n0

        if abs(n0 - n1) > 1:
            return -1

        option1 = [0 if i%2 == 0 else 1 for i in range(0, len(s))]
        option2 = [1 if i%2 == 0 else 0 for i in range(0, len(s))]

        mismatchOption1 = 0
        mismatchOption2 = 0

        for i, c in enumerate(s):
            if int(c) != option1[i]:
                mismatchOption1 +=1
            if int(c) != option2[i]:
                mismatchOption2 +=1
        
        if n0 > n1:
            return mismatchOption1 // 2
        elif n0 < n1:
            return mismatchOption2 // 2
        else:
            return min(mismatchOption1 // 2, mismatchOption2 // 2)
