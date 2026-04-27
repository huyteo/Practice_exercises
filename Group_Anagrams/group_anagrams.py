from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))   # tạo key bằng cách sort
            groups[key].append(s)

        return list(groups.values())


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]

    sol = Solution()
    result = sol.groupAnagrams(strs)

    print("Kết quả:")
    for group in result:
        print(group)