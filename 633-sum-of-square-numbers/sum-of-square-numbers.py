class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c))+1):
            j = sqrt(c-i*i)
            if j == int(j):
                return True
        return False