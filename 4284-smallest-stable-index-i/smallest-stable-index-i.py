class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        n = len(nums)
        while right < n:
            x=max(nums[left:right+1])- min(nums[right:n])
            if x<=k:
                return right
            right += 1
        return -1