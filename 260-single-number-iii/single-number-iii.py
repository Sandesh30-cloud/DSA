class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for num in count:
            if count[num] == 1:
                res.append(num)
        return res