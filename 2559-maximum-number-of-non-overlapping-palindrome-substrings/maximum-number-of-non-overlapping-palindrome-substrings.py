class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        e = -1
        for i in range(n):
            for l in (i -1, i):
                left, right = l, i
                while left >= 0 and right < n and s[left] == s[right]:
                    if right - left + 1 >= k and left > e:
                        res += 1
                        e = right
                        break
                    left -= 1
                    right += 1
        return res