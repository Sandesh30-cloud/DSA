class Solution:
    def checkDivisibility(self, n: int) -> bool:
        orignl = n
        dsum = 0
        dprod = 1
        while n > 0:
            dgt = n % 10
            dsum += dgt
            dprod *= dgt
            n //= 10
        total = dsum + dprod
        return orignl % total == 0