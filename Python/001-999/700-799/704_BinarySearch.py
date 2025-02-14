class Solution:
    def __init__(self) -> None:
        pass

    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

nums1, target1 = [-1,0,3,5,9,12], 9
nums2, target2 = [-1,0,3,5,9,12], 2

s = Solution()
print(s.search(nums1, target1))
print(s.search(nums2, target2))
