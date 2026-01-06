# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        qu = deque([root])
        lev = 1
        maxSum = float('-inf')
        ansLev = 1
        while qu:
            levSum = 0
            for _ in range(len(qu)):
                node = qu.popleft()
                levSum += node.val
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            if levSum > maxSum:
                maxSum = levSum
                ansLev = lev

            lev += 1

        return ansLev