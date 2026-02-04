class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        res = -float('inf')
        i = 1
        while i < len(nums)- 2:
            a = b = i
            net = nums[a]
            while b + 1 < len(nums)and nums[b + 1] < nums[b]:
                net += nums[b + 1]
                b += 1
            if b == a:
                i += 1
                continue
            c = b
            left = right = 0
            lx = rx = -float('inf')
            
            while a - 1 >= 0 and nums[a - 1] < nums[a]:
                left += nums[a - 1]
                lx = max(lx, left)
                a -= 1
            if a == i:
                i += 1
                continue
            
            while b + 1 < len(nums)and nums[b + 1] > nums[b]:
                right += nums[b + 1]
                rx = max(rx, right)
                b += 1
            if b == c:
                i += 1
                continue
                
            res = max(res, lx + rx + net)
            i = b
        return res if res != -float('inf') else 0