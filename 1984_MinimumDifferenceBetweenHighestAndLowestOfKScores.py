class Solution:

    def __init__(self) -> None:
        pass

    def minimumDifference(self, nums: list[int], k: int) -> int:
        """
        This function will return the minimized difference between k scores within an array of n scores.
        First, it will sort the list from smallest to largest, then it will compare a score with its nearest
        neighbour. 

        Because the list is sorted, there is no point making additional checks against other values as within
        a sorted list, the best candidate for a minimized score will always be the difference between any value
        and its preceeding k value/s.

        So, a two pointer algorithm will be implemented to iterate through the list once, compute the differences
        and use a min function to ensure the lowest difference is returned.
        """
        nums.sort()
        l, r = 0, k-1
        res = float("inf")

        while r < len(nums):
            res = min(res, nums[r]-nums[l])
            l += 1
            r += 1
        return res

    

s = Solution()
nums1 = [90]
nums2 = [9,4,1,7]

print(s.minimumDifference(nums= nums1, k=1))

print(s.minimumDifference(nums= nums2, k=2))

