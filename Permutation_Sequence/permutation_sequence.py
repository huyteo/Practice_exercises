import math

class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n + 1))
        k -= 1  # chuyển về 0-based

        result = ""

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)

            index = k // fact
            result += str(nums[index])

            nums.pop(index)

            k %= fact

        return result


if __name__ == "__main__":
    # Nhập dữ liệu từ bàn phím
    n = int(input("Nhập n: "))
    k = int(input("Nhập k: "))

    sol = Solution()
    result = sol.getPermutation(n, k)

    print("Kết quả:", result)