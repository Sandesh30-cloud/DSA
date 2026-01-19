class Solution:
    def maxArea(self, height: List[int]) -> int:
        mw = 0
        l,r = 0, len(height)-1
        while l < r:
            w = r - l
            ht = min(height[l], height[r])
            area = w * ht
            mw= max(mw, area)
            if height[l]<height[r]:
                l += 1
            else: 
                r -= 1
        return mw