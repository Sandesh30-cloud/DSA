class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_gap = 0
        if len(nums) == 1 or len(nums) == 0:
            return 0
        for num in range(1,len(nums)):
            curr = abs(nums[num]- nums[num-1])
            max_gap = max(max_gap, curr) 
        return max_gap