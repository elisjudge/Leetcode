class Solution:
    def __init__(self) -> None:
        pass
    
    def nextGreaterElement1(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        This solution will be in O(n*m) time with O(m) space complexity
        """

        nums1_hash = { num:idx for idx, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1_hash:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1_hash[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

    def nextGreaterElement2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        This solution will be in O(n+m) time with O(m) space complexity
        """

        nums1_hash = { num:idx for idx, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1_hash[val]
                res[idx] = cur
            if cur in nums1_hash:
                stack.append(cur)
        return res


nums1a, nums2a = [4,1,2], [1,3,4,2] #[-1,3,-1]
nums1b, nums2b = [2,4], [1,2,3,4] #[3,-1]

s = Solution()
print("First Solution using hashmap")
print(s.nextGreaterElement1(nums1a, nums2a))
print(s.nextGreaterElement1(nums1b, nums2b))
print()
print("Second Solution using hashmap and stack in o(m+n) time complexity")
print(s.nextGreaterElement2(nums1a, nums2a))
print(s.nextGreaterElement2(nums1b, nums2b))
print()