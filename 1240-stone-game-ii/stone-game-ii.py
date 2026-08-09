from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from piles[i] to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        @lru_cache(None)
        def dp(i, M):
            # The current player can take every remaining pile
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                opponent = dp(i + X, max(M, X))
                current = suffix[i] - opponent
                best = max(best, current)

            return best

        return dp(0, 1)