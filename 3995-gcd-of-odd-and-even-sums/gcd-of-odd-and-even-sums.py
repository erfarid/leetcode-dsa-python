class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n                  
        sumEven = n * (n + 1)           

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        return gcd(sumOdd, sumEven)