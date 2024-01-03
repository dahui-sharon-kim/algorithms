# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"(":")", "{":"}", "[":"]"}
        stack = []
        for ch in s:
            if ch in parens: # 여는 괄호
                stack.append(ch)
            else: # 닫는 괄호
                if not stack or ch != parens[stack.pop()]: # stack이 비어있거나 / 스택의 마지막 아이템에 대응하지 않으면 return False
                    return False
            return not stack # stack이 비어있는 경우에만 return True