class Solution:
    def __init__(self) -> None:
        pass
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1

        if target > nums[r]:
            return r+1
        elif target < nums[l]:
            return l
        

        while l <= r:
            m = (l+r)//2

            if nums[m] > target:
                r = m - 1

            elif nums[m] < target:
                l = m + 1

            else:
                return m
            
        return l




nums1, target1 = [1,3,5,6], 5
nums2, target2 = [1,3,5,6], 2
nums3, target3 = [1,3,5,6], 7
nums4, target4 = [1], 1

s=Solution()
print(s.searchInsert(nums1, target1))
print(s.searchInsert(nums2, target2))
print(s.searchInsert(nums3, target3))
print(s.searchInsert(nums4, target4))