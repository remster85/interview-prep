#https://leetcode.com/problems/two-sum/submissions/1417977061/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        existingNums = set()
        for i, num  in enumerate(nums):
            if num not in numsMap:
                numsMap[num] = []        
            numsMap[num].append(i)
            
            rest = target - num
            if (target - num) in existingNums:
                return [numsMap[rest][0], i]

            existingNums.add(num)
            #print(f"existingNums={existingNums} , numsMap={numsMap}")
        return []
