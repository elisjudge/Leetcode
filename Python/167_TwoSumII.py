class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r, = 0, len(numbers)-1

        while l <= r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r-= 1                
            else:
                l+= 1

s = Solution()

numbers1, target1 = [2,7,11,15], 9
numbers2, target2 = [2,3,4], 6
numbers3, target3 = [5,25,75], 100

print(s.twoSum(numbers3, target3))