from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def dfs(text, opening, closing):
            if opening < closing or opening > n:
                return
            if opening == n and closing == n:
                result.append(text)
                return result
            dfs(text+"(", opening+1, closing)
            dfs(text+")", opening, closing+1)
        
        dfs("", 0, 0)
        return result


solution_instance = Solution()
print(solution_instance.generateParenthesis(3))