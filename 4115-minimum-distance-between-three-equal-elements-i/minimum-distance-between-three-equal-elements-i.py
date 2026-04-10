class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        p = defaultdict(list)
        for i,num in enumerate(nums):
            p[num].append(i)
        res = float('inf')
        for i in p.values():
            if len(i)>=3:
                for j in range(len(i)-2):
                    res = min(res, i[j+2] - i[j])
        return res*2 if res != float('inf') else -1

