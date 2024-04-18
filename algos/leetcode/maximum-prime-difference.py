#https://leetcode.com/problems/maximum-prime-difference/submissions/
class Solution(object):
    
    def is_prime(self, x):
        if x < 2:
            return False
        elif x == 2:
            return True  
        for n in range(2, x):
            if x % n ==0:
                return False
        return True


    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """     
        primes = {}
        
        for i in range(0,100):
            if self.is_prime(i):
                primes[i] = i
        
        mostLeftPrime = -1
        mostRightPrime = -1
        
        
        for i in range(0, len(nums)):
            print(i)
            if mostLeftPrime == -1 and nums[i] in primes:
                mostLeftPrime = i
            if mostRightPrime == -1 and  nums[len(nums)-i - 1] in primes:
                mostRightPrime = len(nums)-i - 1
            if mostRightPrime != - 1 and  mostLeftPrime != -1:
                break        
        
        return mostRightPrime - mostLeftPrime