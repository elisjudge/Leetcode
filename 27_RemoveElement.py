class Solution:

    def __init__(self) -> None:
        pass

    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k



nums1, val1 = [3,2,2,3], 3
nums2, val2 = [0,1,2,2,3,0,4,2], 2



s= Solution()
print(s.removeElement(nums1, val1))
print(s.removeElement(nums2, val2))



