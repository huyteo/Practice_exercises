class Solution:
    def simplifyPath(self, path):
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


def main():
    sol = Solution()

    test_cases = [
        "/home/",
        "/home//foo/",
        "/home/user/Documents/../Pictures",
        "/../",
        "/.../a/../b/c/../d/./"
    ]

    for path in test_cases:
        print(f"Input : {path}")
        print(f"Output: {sol.simplifyPath(path)}")
        print("-" * 40)


if __name__ == "__main__":
    main()