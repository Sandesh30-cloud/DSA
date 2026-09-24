class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for num in range(len(nums)):
            n = nums[num]
            summ = 0
            while n > 0:
                summ += n % 10
                n //=10
            if summ == num:
                return num
        return -1