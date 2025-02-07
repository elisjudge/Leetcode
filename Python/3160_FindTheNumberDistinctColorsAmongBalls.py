from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        balls = {}
        colours = defaultdict(int)
        result = []

        for ball, colour in queries:
            if ball in balls:
                old_colour = balls[ball]
                colours[old_colour] -= 1
                if colours[old_colour] == 0:
                    del colours[old_colour]
            
            balls[ball] = colour
            colours[colour] += 1
            result.append(len(colours))

        return result

s= Solution()

testcases = [
    {"limit": 4, "queries": [[1,4],[2,5],[1,3],[3,4]], "expected": [1,2,2,3]},
    {"limit": 4, "queries": [[0,1],[1,2],[2,2],[3,4],[4,5]], "expected": [1,2,2,3,4]}
]

for i, testcase in enumerate(testcases):
    output = s.queryResults(testcase["limit"], testcase["queries"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    