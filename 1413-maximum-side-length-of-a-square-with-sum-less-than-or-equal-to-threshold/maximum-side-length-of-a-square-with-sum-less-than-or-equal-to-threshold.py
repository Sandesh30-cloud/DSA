class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )
        max_len = 0
        # all possible square sizes
        for size in range(1, min(m, n) + 1):
            for i in range(size, m + 1):
                for j in range(size, n + 1):
                    square_sum = (
                        prefix[i][j]
                        - prefix[i - size][j]
                        - prefix[i][j - size]
                        + prefix[i - size][j - size]
                    )
                    if square_sum <= threshold:
                        max_len = size
                        break
                else:
                    continue
                break

        return max_len