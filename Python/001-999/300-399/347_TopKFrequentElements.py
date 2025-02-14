import heapq

class Solution:
    def topKFrequent_Heap(self, nums: list[int], k: int) -> list[int]:
        """Min Heap Solution O(n logK)"""

        # Count frequencies o(n)
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # Create Heap (o(n logK))
        heap = []
        for key, val in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        
        return [item[1] for item in heap[::-1]] # Need to reverse the heap because we are performing max operation using min heap
    
    def topKFrequent_Bucket(self, nums: list[int], k: int) -> list[int]:
        """Bucket Sort Solution"""
        freq = {}
        val_arrays = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for n, f in freq.items():
            val_arrays[f].append(n)
        
        result = []

        for i in range(len(val_arrays) - 1, 0, -1):
            for n in val_arrays[i]:
               result.append(n)
               if len(result) == k:
                   return result 

test_cases = [
    {"nums": [1,1,1,2,2,3], "k": 2, "expected": [1,2]},
    {"nums": [1], "k": 1, "expected": [1]}
]

s = Solution()

for i, testcase in enumerate(test_cases):
    heap_output = s.topKFrequent_Heap(testcase["nums"], testcase["k"])
    bucket_output = s.topKFrequent_Bucket(testcase["nums"], testcase["k"])

    if heap_output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (Heap): {heap_output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (Heap): {heap_output}")
    
    if bucket_output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (Bucket): {bucket_output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (Bucket): {bucket_output}")
