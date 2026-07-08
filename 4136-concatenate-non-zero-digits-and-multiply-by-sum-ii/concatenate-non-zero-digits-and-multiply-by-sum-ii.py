from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # prefixNZ[i] = number of non-zero digits before index i
        prefixNZ = [0] * (n + 1)

        # values/sums over only non-zero digits
        val = [0]
        digitSum = [0]

        for i, ch in enumerate(s):
            prefixNZ[i + 1] = prefixNZ[i]

            if ch != '0':
                d = int(ch)
                prefixNZ[i + 1] += 1
                val.append((val[-1] * 10 + d) % MOD)
                digitSum.append(digitSum[-1] + d)

        k = len(val) - 1

        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        ans = []

        for l, r in queries:
            left = prefixNZ[l]
            right = prefixNZ[r + 1]

            length = right - left

            if length == 0:
                ans.append(0)
                continue

            x = (val[right] - val[left] * pow10[length]) % MOD
            sm = digitSum[right] - digitSum[left]

            ans.append((x * sm) % MOD)

        return ans