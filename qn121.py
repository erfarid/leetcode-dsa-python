from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      
        mn = min(prices)
        ch = 0  
        val = 0 

        for i in range( len(prices)):
            if prices[i]==mn :
                ch = i
                val = prices[ch]
          
       
        mx = 0 
        if ch != len(prices):
             for i in range (ch , len(prices)):
                 if prices[i] > mx :
                    mx = prices[i]
        else:
            mx = prices[ch]


        return mx -val

sol = Solution()
print(sol.maxProfit([2,4,1]))        


      