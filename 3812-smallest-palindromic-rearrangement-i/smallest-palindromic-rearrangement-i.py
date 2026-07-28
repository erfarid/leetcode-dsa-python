from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        left = []
        middle = ""

        # Characters are checked alphabetically
        for char in "abcdefghijklmnopqrstuvwxyz":
            left.append(char * (count[char] // 2))

            if count[char] % 2 == 1:
                middle = char

        left_half = "".join(left)

        return left_half + middle + left_half[::-1]