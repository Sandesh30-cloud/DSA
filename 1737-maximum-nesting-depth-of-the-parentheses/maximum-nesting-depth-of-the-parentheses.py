class Solution:
    def maxDepth(self, s: str) -> int:
        dep = 0
        ans = 0
        for ch in s:
            if ch == '(':
                dep += 1
            elif ch == ')':
                dep -= 1
            ans = max(ans, dep)
        return ans