class Solution:
    def __init__(self) -> None:
        pass

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        
        print(nums)   


nums1 = [0,1,0,3,12]  # [1,3,12,0,0]
nums2 = [0] # [0]

s=Solution()
s.moveZeroes(nums1)
s.moveZeroes(nums2)