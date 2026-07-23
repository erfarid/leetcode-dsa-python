class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return n
        
        # For n >= 3, all values from 0 to the next power of 2 - 1 are possible
        return 1 << n.bit_length()