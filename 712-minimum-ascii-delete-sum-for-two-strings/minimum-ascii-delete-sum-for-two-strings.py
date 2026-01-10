class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # mindelsum = ascii_sum(s1)+ascii_sum(s2) - 2 x ascii_sum(lcs)
        m, n = len(s1), len(s2)

        # total ascii sum of both strings
        total_sum = 0
        for ch in s1:
            total_sum += ord(ch)
        for ch in s2:
            total_sum += ord(ch)

        # ascii weighted LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return total_sum - 2 * dp[0][0]