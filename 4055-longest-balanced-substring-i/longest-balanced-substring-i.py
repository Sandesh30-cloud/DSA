class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            freq = [0]*26
            dist = 0
            max_freq = 0
            for j in range(i, n):
                indx = ord(s[j]) - ord('a')
                if freq[indx] == 0:
                    dist += 1
                freq[indx] += 1
                max_freq = max(max_freq, freq[indx])
                l = j - i + 1
                if max_freq * dist == l:
                    ans = max(ans, l)
        return ans