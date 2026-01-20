class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = [0] * 26
        count_s = [0] * 26
        result = []
        for c in p:
            count_p[ord(c) - ord('a')] += 1
        for i in range(len(s)):
            count_s[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                count_s[ord(s[i - len(p)]) - ord('a')] -=1
            if count_s == count_p:
                result.append(i - len(p) + 1)
        return result
