class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mindiff = float('inf')
        n = len(nums)
        if k == 1:
            return 0
        for i in range(n - k + 1):
            mindiff = min(mindiff, nums[i + k - 1] - nums[i])
        return mindiff
        