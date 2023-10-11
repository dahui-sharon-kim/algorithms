from typing import List

class Solution:
    def generateParenthesis(self, n:int) -> List[str]:
        result = []

        def dfs(text, opening, closing):
            if opening == n and closing == n:
                result.append(text)
                return
                # return result.append(text)
            if opening > n or opening < closing:
                return
            dfs(text + "(", opening + 1, closing)
            dfs(text + ")", opening, closing + 1)

        dfs("", 0, 0)
        return result

solution_instance = Solution()
print(solution_instance.generateParenthesis(3))