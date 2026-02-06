class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        result = 0
        for i in range(len(nums)):
            while j + 1 < len(nums) and nums[i]*k >= nums[j+1]:
                j += 1
            result = max(result, j - i + 1)
        return len(nums) - result