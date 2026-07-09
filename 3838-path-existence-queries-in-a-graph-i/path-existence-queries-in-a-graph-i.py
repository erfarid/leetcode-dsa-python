from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:
        
        # component[i] tells which connected group node i belongs to
        component = [0] * n
        
        comp_id = 0
        
        for i in range(1, n):
            # If adjacent difference is greater than maxDiff,
            # then connection breaks and new component starts
            if nums[i] - nums[i - 1] > maxDiff:
                comp_id += 1
            
            component[i] = comp_id
        
        answer = []
        
        for u, v in queries:
            answer.append(component[u] == component[v])
        
        return answer