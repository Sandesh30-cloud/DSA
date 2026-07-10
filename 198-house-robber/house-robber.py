class Solution:
    def rob(self, nums: List[int]) -> int:
        pre1= 0
        pre2 = 0
        for n in nums:
            curr = max(pre1, pre2 + n)
            pre2 = pre1
            pre1 = curr
        return curr