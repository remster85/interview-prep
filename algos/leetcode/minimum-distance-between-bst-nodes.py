# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                nums.append(root.val)
                inOrder(root.right)
        inOrder(root)
        
        min = 999999999999
        for i in range(0, len(nums)-1):
            if nums[i+1] - nums[i] < min:
                min = nums[i+1] - nums[i]
        return min
            


        return nums
