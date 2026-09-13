class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        x = ''.join(map(str,nums))
        return x.count(str(digit))