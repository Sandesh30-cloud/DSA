class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = []
        for i in matrix:
            res.append(sum(i))
        return res