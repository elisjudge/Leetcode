class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            if num > 0:
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums [l - 1] and l < r:
                        l += 1
        return res
    
s = Solution()

print(s.threeSum(nums=[-1,0,1,2,-1,-4]))
print(s.threeSum(nums=[0,1,1]))
print(s.threeSum(nums=[0,0,0]))