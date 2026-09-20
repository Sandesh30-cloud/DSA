class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = []
        nums.sort()
        for num in range(len(nums)-1):
            if nums[num+1] - nums[num]> 1:
                for j in range(nums[num]+1, nums[num+1]):
                    a.append(j)
        return a