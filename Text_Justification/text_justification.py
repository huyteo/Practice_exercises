class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            # ===== 1. Gom từ =====
            line_len = len(words[i])
            j = i + 1

            while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = len(line_words)

            # ===== 2. Xử lý dòng =====
            # Trường hợp: dòng cuối hoặc chỉ có 1 từ
            if j == len(words) or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:
                total_chars = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_chars
                slots = num_words - 1

                space_each = total_spaces // slots
                extra = total_spaces % slots

                line = ""
                for k in range(slots):
                    line += line_words[k]
                    # slot bên trái được cộng thêm 1 space nếu còn dư
                    spaces = space_each + (1 if k < extra else 0)
                    line += " " * spaces

                line += line_words[-1]

            res.append(line)
            i = j

        return res


# ===== MAIN để chạy trong VSCode =====
def main():
    sol = Solution()

    test_cases = [
        (
            ["This", "is", "an", "example", "of", "text", "justification."],
            16
        ),
        (
            ["What","must","be","acknowledgment","shall","be"],
            16
        ),
        (
            ["Science","is","what","we","understand","well","enough","to",
             "explain","to","a","computer.","Art","is","everything","else","we","do"],
            20
        )
    ]

    for idx, (words, maxWidth) in enumerate(test_cases, 1):
        print(f"\n===== Test case {idx} =====")
        print(f"maxWidth = {maxWidth}")

        result = sol.fullJustify(words, maxWidth)

        for line in result:
            # in dấu | để thấy rõ khoảng trắng
            print(f"|{line}|  -> length = {len(line)}")


if __name__ == "__main__":
    main()