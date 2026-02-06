class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        mask = 0
        max_len = 0
        for r in range(n):
            while (mask & nums[r]) != 0:
                mask ^= nums[l]
                l += 1
            mask |= nums[r]
            max_len = max(max_len, r-l+1)
        return max_len
