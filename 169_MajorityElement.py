class Solution:
    def __init__(self) -> None:
        pass

    def boyerMooreMajorityElement(self, nums: list[int]) -> int:
        """
        This will solve the problem using o(1) space. However,
        this iteration will only be accurate if it is fed a 
        case that has a majority element. If no majority element exists,
        then a different iteration would be needed.
        """

        res, count = 0, 0 

        for n in nums:
            if not count:
                res = n
           
            count += (1 if n == res else -1)
        return res


    def majorityElement(self, nums: list[int]) -> int:
        hashmap = {}
        majority = None

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

            if hashmap[nums[i]] > (i/2):
                majority = nums[i]

        return majority

nums1 = [3,2,3]   
nums2 = [2,2,1,1,1,2,2]

s = Solution()
print("Solution with hashmap in O(n) time and O(n) space")
print(s.majorityElement(nums1))
print(s.majorityElement(nums2))
print()
print("Solution using Boyer-Moore Majority Vote Algorithm in O(n) time and O(1) space")
print(s.boyerMooreMajorityElement(nums1))
print(s.boyerMooreMajorityElement(nums2))