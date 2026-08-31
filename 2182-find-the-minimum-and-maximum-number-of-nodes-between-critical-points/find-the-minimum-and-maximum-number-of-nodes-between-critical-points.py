# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = -1
        prev_critical = -1
        min_dist = float('inf')
        max_dist = -1

        while curr and curr.next:
            # Check if curr is a critical point
            if ((prev.val < curr.val > curr.next.val) or
                (prev.val > curr.val < curr.next.val)):

                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - prev_critical)

                    # Distance from first critical point
                    max_dist = pos - first

                prev_critical = pos

            prev = curr
            curr = curr.next
            pos += 1

        if max_dist == -1:
            return [-1, -1]

        return [min_dist, max_dist]