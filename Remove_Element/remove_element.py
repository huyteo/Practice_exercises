class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        i = 0
        
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        
        return n


# ====== TEST CODE ======
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2

    print("Before:", nums)

    sol = Solution()
    k = sol.removeElement(nums, val)

    print("After:", nums)
    print("k =", k)
    print("Valid elements:", nums[:k])