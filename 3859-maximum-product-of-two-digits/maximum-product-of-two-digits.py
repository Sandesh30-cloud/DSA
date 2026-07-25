class Solution:
    def maxProduct(self, n: int) -> int:
        dig = sorted(int(d) for d in str(n))
        return dig[-1] * dig[-2]