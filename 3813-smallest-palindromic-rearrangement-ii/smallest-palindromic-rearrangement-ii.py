from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        mid = ""
        half = [0] * 26
        total = 0

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ord(ch) - ord('a')] = cnt // 2
            total += cnt // 2

        LIMIT = k

        def count_perm(cnts, n):
            """Number of distinct permutations of multiset (capped at LIMIT)."""
            res = 1
            rem = n
            for c in cnts:
                if c:
                    res *= comb(rem, c)
                    if res > LIMIT:
                        return LIMIT
                    rem -= c
            return res

        if count_perm(half, total) < k:
            return ""

        first = []

        while total:
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count_perm(half, total - 1)

                if ways >= k:
                    first.append(chr(i + ord('a')))
                    total -= 1
                    break
                else:
                    k -= ways
                    half[i] += 1

        first = "".join(first)
        return first + mid + first[::-1]