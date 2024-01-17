from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations = []
        def dfs(picked, unpicked):
            if (not unpicked):
                permutations.append(picked)
                return
            for i, num in enumerate(unpicked):
                dfs(picked + [num], unpicked[:i] + unpicked[i+1 :])
        dfs([], nums)
        return permutations            
        

sol = Solution()
print(sol.permute([1, 2, 3]))