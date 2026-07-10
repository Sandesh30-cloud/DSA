class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast, n in enumerate(nums):
            if n != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1
        

        