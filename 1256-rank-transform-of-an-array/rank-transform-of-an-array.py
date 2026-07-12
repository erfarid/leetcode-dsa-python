from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # make a sorted list of unique values
        sorted_arr = sorted(set(arr))
        
        # create rank dictionary
        rank = {}
        for i in range(len(sorted_arr)):
            rank[sorted_arr[i]] = i + 1
        
        # replace each element with its rank
        result = []
        for num in arr:
            result.append(rank[num])
        
        return result