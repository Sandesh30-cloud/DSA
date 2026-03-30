class Solution:
    def reverseDegree(self, s: str) -> int:
        res, ind = 0,1
        for i in s:
            res += (123-ord(i)) * ind
            ind += 1
        return res