class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        blocks = [len(i) for i in s.split("1") if i]
        res = 0
        for i in range(len(blocks)-1):
            res = max(res,blocks[i]+blocks[i+1])
        return s.count("1") + res