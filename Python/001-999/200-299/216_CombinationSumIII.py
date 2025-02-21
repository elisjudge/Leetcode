class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []

        def backtracking(i:int, curr_arr:list, curr_sum:int):
            if len(curr_arr) == k and curr_sum == n:
                res.append(curr_arr.copy())
                return 
            elif len(curr_arr) == k:
                return
            elif curr_sum > n:
                return
            
            for val in range(i, 10):
                if curr_sum + val > n:
                    return
                backtracking(val + 1, curr_arr + [val], curr_sum + val)

        backtracking(1, [], 0)
        return res


s = Solution()

testcases = [
    {"k": 3, "n": 7, "expected": [[1,2,4]]},
    {"k": 3, "n": 9, "expected": [[1,2,6],[1,3,5],[2,3,4]]},
    {"k": 4, "n": 1, "expected": []}
]

for i, testcase in enumerate(testcases):
    output = s.combinationSum3(testcase["k"],testcase["n"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   
