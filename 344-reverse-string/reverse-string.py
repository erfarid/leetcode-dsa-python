class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
       
        y = len(s)-1
        for i in range(len(s)//2):
            s[i] ,s[y] =s[y] ,s[i]
            y-=1

        return s   

        