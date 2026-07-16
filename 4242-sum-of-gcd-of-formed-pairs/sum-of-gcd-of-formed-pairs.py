from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mx = 0
        
        # Construct prefixGcd
        for num in nums:
            mx = max(mx, num)
            prefixGcd.append(gcd(num, mx))
        
        # Sort the array
        prefixGcd.sort()
        
        # Pair smallest with largest and calculate gcd sum
        ans = 0
        left, right = 0, len(prefixGcd) - 1
        
        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        
        return ans