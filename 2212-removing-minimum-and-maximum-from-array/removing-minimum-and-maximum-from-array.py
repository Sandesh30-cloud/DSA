class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        l = min(min_idx, max_idx)
        r = max(min_idx, max_idx)

        n = len(nums)

        left = r+1
        right = n-l
        both = (l+1)+(n-r)
        return min(left,right,both)

    
    

