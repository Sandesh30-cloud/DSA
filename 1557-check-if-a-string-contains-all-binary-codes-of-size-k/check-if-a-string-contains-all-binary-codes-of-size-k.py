class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # return (number of substrings of length k == 2**k)
        n = len(s)
        ans = set()
        i = 0
        j = k-1
        while j < n:
            ans.add(s[i:j+1])
            j +=1
            i+=1
        return len(ans)==2**k