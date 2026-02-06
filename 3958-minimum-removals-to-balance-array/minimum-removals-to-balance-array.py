class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        for i in range(len(nums)):
            if nums[i] > nums[l] * k:
                l += 1
        return l