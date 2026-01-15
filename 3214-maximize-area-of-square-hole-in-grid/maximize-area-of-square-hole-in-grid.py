class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        maxH, maxV, maximum = 1,1,1
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i-1] == 1:
                maximum += 1
            else:
                maxH = max(maxH, maximum)
                maximum = 1
        maxH = max(maxH, maximum)
        maximum = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i-1] == 1:
                maximum += 1
            else:
                maxV = max(maxV, maximum)
                maximum = 1
        maxV = max(maxV, maximum)
        result = min(maxH + 1, maxV + 1)
        return result * result

        