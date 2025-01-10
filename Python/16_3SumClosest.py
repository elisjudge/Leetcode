class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
               curr = num + nums[l] + nums[r]
               if curr == target:
                   return curr
               if abs(curr - target) < abs(closest - target):
                    closest = curr    
               if curr < target:
                   l += 1
               elif curr > target:
                   r -= 1

        return closest

s = Solution()

print(s.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(s.threeSumClosest(nums = [0,0,0], target = 1))