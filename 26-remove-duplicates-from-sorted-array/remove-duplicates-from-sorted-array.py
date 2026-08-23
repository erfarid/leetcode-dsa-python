

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #  for i in range(1, len(nums)):
        #     if nums[i]!=nums[i-1]:
        #         nums[k] = nums[i]
        #         k+=1
        #  return k     

        k = 1
        for num in nums:
            if k == 0 or nums[k-1] != num :
                nums[k]= num
                k+=1
        return k 

        
        