class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        w = valueDiff + 1
        for i, num in enumerate(nums):
            b = num // w
            if b in buckets or buckets.get(b-1, float('-inf')) >= num - valueDiff or buckets.get(b+1, float('inf')) <= num + valueDiff:
                return True
            buckets[b] = num
            if i >= indexDiff:
                del buckets[nums[i-indexDiff] // w]
        return False