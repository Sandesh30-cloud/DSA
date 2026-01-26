class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n_set = set(nums)
        max_len = 1
        for num in n_set:
            if num-1 not in n_set:
                i = 1
                while num+i in n_set:
                    i +=1
                    max_len= max(i, max_len)
        return max_len
