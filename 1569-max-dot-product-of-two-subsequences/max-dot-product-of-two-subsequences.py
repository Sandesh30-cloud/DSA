class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        if m > n:
            return self.maxDotProduct(nums2,nums1)
        dp = [float('-inf')] * (m+1)
        for i in range(1, n+1):
            prev = float('-inf')
            for j in range(1, m+1):
                curr = nums1[i-1]*nums2[j-1]
                temp = dp[j]
                dp[j] = max(curr, curr + prev, dp[j], dp[j-1])
                prev = temp
        return dp[m]