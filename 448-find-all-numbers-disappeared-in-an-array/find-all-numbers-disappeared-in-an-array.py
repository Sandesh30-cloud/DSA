class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        cons = []
        # for i in range(1, len(nums)+1):
        #     if i not in nums:
        #         cons.append(i)
        # return cons
        seen =set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in seen:
                res.append(i)
        return res