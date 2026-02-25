class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            print("\nBắt đầu vòng mới:")
            print(f"dividend = {dividend}")

            while dividend >= (temp << 1):
                print(f"  temp <<= 1: {temp} -> {temp << 1}")
                temp <<= 1
                multiple <<= 1

            print(f"  Trừ temp = {temp}, cộng multiple = {multiple}")

            dividend -= temp
            result += multiple

            print(f"  Sau khi trừ: dividend = {dividend}, result = {result}")

        return -result if negative else result


if __name__ == "__main__":
    solution = Solution()

    dividend = 50
    divisor = 3

    print("KẾT QUẢ CUỐI CÙNG:")
    print(solution.divide(dividend, divisor))