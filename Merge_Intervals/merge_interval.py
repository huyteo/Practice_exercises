class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        result = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                result.append(prev)
                prev = curr

        result.append(prev)
        return result


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    sol = Solution()
    result = sol.merge(intervals)

    print("Kết quả sau khi merge:", result)