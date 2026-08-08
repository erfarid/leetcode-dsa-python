from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # last[j] = the last index in word1 where word2[j]
        # can be matched while matching word2[j..m-1].
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        can_change = True

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed mismatch
            elif can_change:
                # After using mismatch at i,
                # word2[j+1:] must be matched exactly.
                #
                # We need to make sure the next character
                # can still be matched after i.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    can_change = False

        if j == m:
            return ans

        return []