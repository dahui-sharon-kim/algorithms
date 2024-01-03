class Solution:
    def generateParenthesis(self, n):
        result = []
        def dfs(text, openingN, closingN):
            if openingN == n and closingN == n:
                result.append(text)
                return
            if (openingN < closingN or openingN > n):
                return
            dfs(text + "(", openingN + 1, closingN)
            dfs(text + ")", openingN, closingN + 1)
        
        dfs("", 0, 0)
        return result

solution_instance = Solution()

print(solution_instance.generateParenthesis(4))