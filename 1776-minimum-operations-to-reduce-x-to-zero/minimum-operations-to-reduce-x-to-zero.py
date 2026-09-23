class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        k = sum(nums)-x
        best = -1
        if k < 0:
            return -1
        b = i = 0
        for j, num in enumerate(nums):
            b += num
            while b > k:
                b -=nums[i]
                i += 1
            if b == k:
                best = max(best, j-i+1)
        return -1 if best < 0 else len(nums) - best
            

            