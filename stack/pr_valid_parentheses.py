class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for ch in s:
            if ch in parens: # 여는 괄호
                stack.append(ch)
            else: # 닫는 괄호
                if not stack or ch != parens[stack.pop()]:
                    return False
        return not stack 

    