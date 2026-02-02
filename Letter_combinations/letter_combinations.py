class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(index, path):
            print(f"DEBUG → index={index}, path='{path}'")

            if index == len(digits):
                print(f"ADD RESULT → {path}")
                res.append(path)
                return

            letters = phone[digits[index]]

            for ch in letters:
                backtrack(index + 1, path + ch)

        backtrack(0, "")
        return res


if __name__ == "__main__":
    s = Solution()
    result = s.letterCombinations("23")
    print("FINAL RESULT:", result)
