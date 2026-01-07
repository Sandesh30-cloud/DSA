# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.ans = 0
        def getTotal(node):
            if not node:
                return 0
            return node.val + getTotal(node.left) + getTotal(node.right)

        total = getTotal(root)

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            sub_sum = node.val + left + right
            self.ans = max(self.ans, sub_sum * (total - sub_sum))
            return sub_sum
        dfs(root)
        return self.ans % MOD
