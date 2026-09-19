class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reversed_str = ""
        for i in range(0,len(s),2*k):
            reversed_str += s[i:i+k][::-1]
            reversed_str += s[i+k:i+2*k]
        return reversed_str