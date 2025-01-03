#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        minLevel = 1
        maxSum = float('-inf')

        queue = deque()
        queue.append(root)

        level = 1

        while queue:
            levelSum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                levelSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelSum > maxSum:
                maxSum = levelSum
                minLevel = level
            level += 1
        return minLevel