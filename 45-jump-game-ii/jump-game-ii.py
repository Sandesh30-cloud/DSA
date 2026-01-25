# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         goal = len(nums) - 1
#         for i in range(len(nums)-2,-1,-1):
#             if i + nums[i] >= goal:
#                 goal = i
#         if goal == 0:
#             return True
#         else:
#             return False
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        far = 0

        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])

            if i == curr_end:
                jumps += 1
                curr_end = far

        return jumps