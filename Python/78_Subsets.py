class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def depth_first_search(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            depth_first_search(i + 1)

            subset.pop()
            depth_first_search(i + 1)

        depth_first_search(0)
        return res

s = Solution()

print(s.subsets([1,2,3]))