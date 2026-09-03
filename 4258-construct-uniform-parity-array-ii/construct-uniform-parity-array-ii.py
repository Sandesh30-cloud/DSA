class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = float('inf')
        for n in nums1:
            if n % 2 == 1:
                odd = min(odd, n)
        if odd == float('inf'):
            return True
        for n in nums1:
            if n % 2 == 0 and n <= odd:
                return False
        return True
