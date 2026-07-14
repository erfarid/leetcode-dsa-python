from typing import List
from math import gcd


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)

        # dp[g1][g2] = number of assignments whose two subsequences
        # currently have GCDs g1 and g2.
        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        dp[0][0] = 1

        for x in nums:
            new_dp = [row[:] for row in dp]  # Choice 1: do not use x

            for g1 in range(max_val + 1):
                for g2 in range(max_val + 1):
                    count = dp[g1][g2]
                    if count == 0:
                        continue

                    # Choice 2: add x to seq1
                    new_g1 = gcd(g1, x)
                    new_dp[new_g1][g2] = (
                        new_dp[new_g1][g2] + count
                    ) % MOD

                    # Choice 3: add x to seq2
                    new_g2 = gcd(g2, x)
                    new_dp[g1][new_g2] = (
                        new_dp[g1][new_g2] + count
                    ) % MOD

            dp = new_dp

        # g > 0 ensures that both subsequences are non-empty.
        return sum(dp[g][g] for g in range(1, max_val + 1)) % MOD