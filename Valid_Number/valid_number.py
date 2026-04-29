class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        num_seen = False
        dot_seen = False
        e_seen = False

        for i, ch in enumerate(s):

            # 1. Nếu là số
            if ch.isdigit():
                num_seen = True

            # 2. Nếu là dấu + hoặc -
            elif ch in ['+', '-']:
                # chỉ hợp lệ nếu ở đầu hoặc sau e/E
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            # 3. Nếu là dấu .
            elif ch == '.':
                # không được có nhiều dấu . hoặc sau e
                if dot_seen or e_seen:
                    return False
                dot_seen = True

            # 4. Nếu là e hoặc E
            elif ch in ['e', 'E']:
                # phải có số trước đó và chưa có e
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False  # cần số phía sau e

            # 5. Ký tự không hợp lệ
            else:
                return False

        return num_seen


def main():
    sol = Solution()

    test_cases = [
        "2",
        "0089",
        "-0.1",
        "+3.14",
        "4.",
        "-.9",
        "2e10",
        "-90E3",
        "3e+7",
        "+6e-1",
        "53.5e93",
        "-123.456e789",
        "abc",
        "1a",
        "1e",
        "e3",
        "99e2.5",
        "--6",
        "-+3",
        ".",
        ""
    ]

    print("Kết quả kiểm tra:\n")
    for s in test_cases:
        print(f"'{s}' -> {sol.isNumber(s)}")


if __name__ == "__main__":
    main()