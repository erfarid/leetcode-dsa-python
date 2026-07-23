class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        active = s.count("1")
        t = "1" + s + "1"

        runs = []
        start = 0

        # Store each block as: [character, block length]
        for i in range(1, len(t)):
            if t[i] != t[start]:
                runs.append((t[start], i - start))
                start = i

        runs.append((t[start], len(t) - start))

        max_gain = 0

        # Look for pattern: zero block + one block + zero block
        for i in range(1, len(runs) - 1):
            if (
                runs[i][0] == "1"
                and runs[i - 1][0] == "0"
                and runs[i + 1][0] == "0"
            ):
                gain = runs[i - 1][1] + runs[i + 1][1]
                max_gain = max(max_gain, gain)

        return active + max_gain