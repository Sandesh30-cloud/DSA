class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = nums[0]
        curr_sum = nums[0]
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(curr_sum+nums[i],nums[i])
            summ = max(curr_sum, summ)
        return summ
        