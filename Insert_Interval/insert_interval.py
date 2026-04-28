class Solution:
    def insert(self, intervals, newInterval):
        result = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)

            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)
        return result


if __name__ == "__main__":
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]

    sol = Solution()
    result = sol.insert(intervals, newInterval)

    print("Kết quả:", result)