class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit = []
        x = n 
        while n > 0:
            digit.append( n % 10)   
            n//=10   
        sum = 0   
        prod =1 
        for i in range(0 , len(digit)):
            sum  += digit[i]
            prod *= digit[i]

        final = sum + prod


        return x % final ==0     


        