class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]
        h_dist = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_dist.add(h[j] - h[i])
        max_side = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in h_dist:
                    max_side = max(max_side, d)
        if max_side == -1:
            return -1
        return (max_side * max_side) % MOD