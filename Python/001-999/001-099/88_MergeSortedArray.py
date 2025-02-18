class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[end] = nums1[m-1]
                m -= 1
            else:
                nums1[end] = nums2[n-1]
                n -= 1
            end -= 1
        
        while n > 0:
            nums1[end] = nums2[n-1]
            n -= 1
            end -= 1

s = Solution()

testCases = [
    {"nums1": [1,2,3,0,0,0], "m": 3, "nums2": [2,5,6], "n": 3, "expected": [1,2,2,3,5,6]},
    {"nums1": [1], "m": 1, "nums2": [], "n": 0, "expected": [1]},
    {"nums1": [0], "m": 0, "nums2": [1], "n": 1, "expected": [1]},
]

for i, testcase in enumerate(testCases):
    output = testcase["nums1"] 
    s.merge(output, testcase["m"], testcase["nums2"], testcase["n"])
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
