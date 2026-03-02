class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len


if __name__ == "__main__":
    test_cases = [
        "(()",
        ")()())",
        "",
        "()()",
        "((()))"
    ]

    solution = Solution()

    for s in test_cases:
        print("\nInput:", s)
        result = solution.longestValidParentheses(s)
        print("Longest valid parentheses length:", result)