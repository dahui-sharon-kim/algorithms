class Solution:
    def longestPalindrome(self, text: str) -> str:
        def is_palindrome(start, end):
            while start < end:
                if text[start] != text[end]:
                    return False
                start, end = start + 1, end - 1
            return True
        
        max_start, max_end = 0, 0

        for start in range(len(text)):
            for end in range(start, len(text)):
                if is_palindrome(start, end) and max_end - max_start < end - start:
                    max_start, max_end = start, end

        return text[max_start : max_end + 1]

sol = Solution()
print(sol.longestPalindrome("hello, world"))