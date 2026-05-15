class Solution:
    def removeDuplicates(self, nums):

        # nếu mảng có <= 2 phần tử
        if len(nums) <= 2:
            return len(nums)

        # vị trí để ghi phần tử hợp lệ
        k = 2

        # duyệt từ phần tử thứ 3
        for i in range(2, len(nums)):

            # chỉ thêm nếu chưa vượt quá 2 lần
            if nums[i] != nums[k - 2]:

                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":

    nums = [1,1,1,2,2,3]

    sol = Solution()

    k = sol.removeDuplicates(nums)

    print("k =", k)
    print("Mảng sau xử lý:", nums[:k])