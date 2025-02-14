class Solution:
    def __init__(self) -> None:
        pass

    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        l = 0
        
        while n < len(nums):
            res.append(nums[l])
            res.append(nums[n])
            l+=1
            n+=1

        return res
    
    def fasterShuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        for i in range(n):
            res += [nums[i], nums[i + n]]
        return res


nums1, n1 = [2,5,1,3,4,7], 3
nums2, n2 = [1,2,3,4,4,3,2,1], 4       
nums3, n3 = [1,1,2,2], 2 

s=Solution()

print(s.fasterShuffle(nums1, n1))
print(s.fasterShuffle(nums2, n2))
print(s.fasterShuffle(nums3, n3))
