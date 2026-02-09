class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(current, open_count, close_count):
            print(f"CALL: current='{current}', open={open_count}, close={close_count}")

            if open_count == n and close_count == n:
                print(f" ADD RESULT: {current}")
                res.append(current)
                return

            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print("KẾT QUẢ CUỐI:")
    print(s.generateParenthesis(3))
