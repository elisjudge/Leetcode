class Solution:

    def __init__(self) -> None:
        pass

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """ This will iterate over every num in nums and check if 
        a value that equates to target minus num exists in the dictionary
        It will begin with an empty dictionary first and the first num 
        will be checked against the empty dictionary before adding it and
        moving onto the next num in all cases.
        This will avoid a problem of using the same element twice to 
        find the target.
        """

        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in hashMap:
                # print([hashMap[diff], i])
                return [hashMap[diff], i]
            hashMap[n] = i
        return


nums = [[2,7,11,15], [3,2,4], [3,3]]
targets = [9, 6, 6]

s = Solution()

for num, target in zip(nums, targets):
    s.twoSum(num, target)