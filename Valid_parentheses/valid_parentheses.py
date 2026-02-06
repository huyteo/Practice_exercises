class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in '([{':
                stack.append(ch)
                print("Push:", ch, "→ Stack:", stack)

            else:
                if not stack:
                    print("Stack rỗng khi gặp", ch)
                    return False

                top = stack.pop()
                print("Pop:", top, "→ Stack:", stack)

                if top != pairs[ch]:
                    print("Sai cặp:", top, "và", ch)
                    return False

        print("Kết thúc – Stack:", stack)
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    test = "([])"
    print("Input:", test)
    print("Kết quả:", s.isValid(test))
