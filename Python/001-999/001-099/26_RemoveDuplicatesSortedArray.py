class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 1
        n = len(nums)
        k = 1

        if n == 1:
            print(nums)
            return k

        while r < n:
            if nums[l] == nums[r]:
                r+= 1
            elif nums[l] != nums[r]:
                nums[k] = nums[r]
                k+= 1
                l = r
                r += 1
        print(nums)
        return k

s= Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))