class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletion = 0
        for ch in s:
            if ch == 'a':
                deletion = min(deletion + 1, b_count)
            else:
                b_count += 1
        return deletion