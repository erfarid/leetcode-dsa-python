# Remove element 


# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# Given an integer array nums and an integer val, 
# remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k,
# to get accepted, you need to do the following things:

from typing import List

def removeElement(nums: List[int] , val:int) -> int :
    k=0
    for num in nums:
        if num!=val:
            nums[k] =num
            k+=1
    return k 
        

print(removeElement([1,2,2,2,3] , 2 ))
         

