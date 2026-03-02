class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
        
        left = i + 1
        right = n - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



if __name__ == "__main__":
    nums = [1, 2, 3, 6, 5, 4]

    print("Before:", nums)

    solution = Solution()
    solution.nextPermutation(nums)

    print("After:", nums)