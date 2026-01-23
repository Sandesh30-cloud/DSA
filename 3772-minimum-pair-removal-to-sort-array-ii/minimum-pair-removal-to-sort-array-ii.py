from heapq import heappush, heappop

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.prev = None
        self.next = None
        self.active = True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        nodes = [Node(val, i) for i, val in enumerate(nums)]
        for i in range(1, n):
            nodes[i].prev = nodes[i - 1]
            nodes[i - 1].next = nodes[i]

        def isViolation(a, b):
            return a.val > b.val

        violationCount = 0
        cur = nodes[0]
        while cur and cur.next:
            if isViolation(cur, cur.next):
                violationCount += 1
            cur = cur.next

        if violationCount == 0:
            return 0

        heap = []
        counter = 0

        def pushPair(left, right):
            nonlocal counter
            if left and right and left.active and right.active and left.next == right:
                heappush(heap, (left.val + right.val, left.idx, counter, left, right))
                counter += 1

        cur = nodes[0]
        while cur and cur.next:
            pushPair(cur, cur.next)
            cur = cur.next

        ops = 0
        while violationCount > 0:
            while heap:
                pairSum, pairIdx, cnt, left, right = heappop(heap)
                if left.active and right.active and left.next == right:
                    break
            else:
                break

            leftPrev = left.prev
            rightNext = right.next

            if leftPrev and leftPrev.active and leftPrev.next == left:
                if isViolation(leftPrev, left):
                    violationCount -= 1

            if rightNext and right.active and right.next == rightNext:
                if isViolation(right, rightNext):
                    violationCount -= 1

            if isViolation(left, right):
                violationCount -= 1

            newVal = left.val + right.val
            newNode = Node(newVal, left.idx)
            newNode.prev = leftPrev
            newNode.next = rightNext

            if leftPrev:
                leftPrev.next = newNode
            if rightNext:
                rightNext.prev = newNode

            left.active = False
            right.active = False
            newNode.active = True

            if leftPrev and leftPrev.active:
                if isViolation(leftPrev, newNode):
                    violationCount += 1
                pushPair(leftPrev, newNode)

            if rightNext and rightNext.active:
                if isViolation(newNode, rightNext):
                    violationCount += 1
                pushPair(newNode, rightNext)

            ops += 1

            if not newNode.prev and not newNode.next:
                violationCount = 0

        return ops