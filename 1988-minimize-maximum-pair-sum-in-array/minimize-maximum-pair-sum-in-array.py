class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0, len(nums) -1
        summ = float('-inf')
        while l < r:
            curr_pair = nums[l] + nums[r]
            summ = max(summ, curr_pair)
            l += 1
            r -= 1
        return summ