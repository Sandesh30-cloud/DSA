class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        seen = [0]*(n+1)
        ans = []
        com = 0
        for i in range(n):
            if seen[A[i]] == 0:
                seen[A[i]] = 1
            elif seen[A[i]] == 1:
                com += 1
            if seen[B[i]] == 0:
                seen[B[i]] = 1
            elif seen[B[i]] == 1:
                com +=1
            ans.append(com)
        return ans