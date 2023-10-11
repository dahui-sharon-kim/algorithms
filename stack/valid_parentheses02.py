class Solution:
    def isValid(self, s: str) -> bool:
        opening = "([{"
        closing = ")]}"
        parens = dict(zip(opening, closing))
        stack = []
        for ch in s:
            if ch in opening:
                stack.append(ch)
            elif ch in closing:
                if not stack or ch != parens[stack.pop()]: # stack이 비어있거나 / 스택의 마지막 아이템에 대응하지 않으면 return False
                    return False
        return not stack # stack이 비어있는 경우에만 return True


solution_instance = Solution()
print(solution_instance.isValid("()"))