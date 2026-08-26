class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
        for i, ch in enumerate(s):
            if ch == '1':
                ones.append(i)
        if len(ones) < k:
            return ""
        res = None
        for i in range(len(ones)-k+1):
            left = ones[i]
            right = ones[i+k-1]
            cand = s[left:right+1]
            if res is None or len(cand) < len(res):
                res = cand
            elif len(cand) == len(res):
                res = min(res, cand)
        return res
        