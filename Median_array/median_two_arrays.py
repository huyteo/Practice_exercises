class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Luôn đảm bảo nums1 là mảng nhỏ hơn
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1


# ===== PHẦN CHẠY TEST =====
if __name__ == "__main__":
    solution = Solution()

    tests = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([0, 0], [0, 0]),
        ([], [1]),
        ([2], [])
    ]

    for nums1, nums2 in tests:
        print("nums1 =", nums1)
        print("nums2 =", nums2)
        print("Median =", solution.findMedianSortedArrays(nums1, nums2))
        print("-" * 30)
