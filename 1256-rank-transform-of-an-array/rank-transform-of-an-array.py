from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Get sorted unique elements
        sorted_unique = sorted(set(arr))
        
        # Step 2: Assign ranks
        rank_map = {num: i + 1 for i, num in enumerate(sorted_unique)}
        
        # Step 3: Replace each element with its rank
        return [rank_map[num] for num in arr]