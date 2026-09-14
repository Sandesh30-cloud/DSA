class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l = max(rec1[0], rec2[0])
        r = min(rec1[2], rec2[2])
        btm = max(rec1[1], rec2[1])
        top = min(rec1[3], rec2[3])

        return l<r and btm<top