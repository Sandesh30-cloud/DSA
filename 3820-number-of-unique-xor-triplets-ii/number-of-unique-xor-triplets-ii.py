class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX = 2048
        pair = [False] * MAX
        ans = [False] * MAX
        for a in nums:
            for b in nums:
                pair[a ^ b] = True
        for x in range(MAX):
            if pair[x]:
                for c in nums:
                    ans[x ^ c] = True
        return sum(ans)