class Solution:
    def __init__(self) -> None:
        pass

    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
       
        return False



nums = [[1,2,3,1], 
        [1,2,3,4], 
        [1,1,1,3,3,4,3,2,4,2]
        ]

s = Solution()

for num in nums:
    print(s.containsDuplicate(num))