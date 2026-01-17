class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        a = 0
        for i in range(n):
            a += i * nums[i]
        val = [a] * n
        for i in range(1, n):
            val[i] = val[i-1] + (n-1)* nums[(i-1) % n] - (total-nums[(i-1) % n])
        return max(val)