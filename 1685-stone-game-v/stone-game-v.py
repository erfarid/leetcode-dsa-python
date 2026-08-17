from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        if n <= 1:
            return 0

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        left_best = [[0] * n for _ in range(n)]
        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                total = prefix[j + 1] - prefix[i]

                # left_sum <= right_sum
                limit = prefix[i] + total // 2

                pos = bisect_right(
                    prefix,
                    limit,
                    i + 1,
                    j + 1
                ) - 1

                if pos >= i + 1:
                    k = pos - 1
                    dp[i][j] = max(
                        dp[i][j],
                        left_best[i][k]
                    )

                # right_sum <= left_sum
                limit = prefix[i] + (total + 1) // 2

                pos = bisect_left(
                    prefix,
                    limit,
                    i + 1,
                    j + 1
                )

                if pos <= j:
                    dp[i][j] = max(
                        dp[i][j],
                        right_best[pos][j]
                    )

                interval_sum = total

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    dp[i][j] + interval_sum
                )

                right_best[i][j] = max(
                    right_best[i + 1][j],
                    dp[i][j] + interval_sum
                )

        return dp[0][n - 1]