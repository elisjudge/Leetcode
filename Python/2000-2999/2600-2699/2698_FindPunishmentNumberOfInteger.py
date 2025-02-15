class Solution:
    def punishmentNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        punishment_num = 1

        def part_sum(num, target, left, right):
            if left + right == target:
                return num * num
            if left == 0:
                return 0
            div = 10
            sub_left = left
            

            while sub_left > 0:
                sub_right = left % div
                sub_left = left // div
                target -= right
                res = part_sum(num, target, sub_left, sub_right)
                if res:
                    return res
                else:
                    target += right
                div *= 10    
            
            return 0

        for i in range(2, n + 1):
            square_i = i * i
            left = square_i
            div = 10

            while left > 0:
                right = square_i % div 
                left = square_i // div 
                if left:
                    res = part_sum(i, i, left, right) 
                    if res:
                        punishment_num += res
                        break
                    div *= 10

        return punishment_num

s= Solution()

testcases = [
    # {"n": 10, "expected": 182},
    {"n": 37, "expected": 1478},
    {"n": 45, "expected": 3503},
    {"n": 55, "expected": 6528},
    {"n": 82, "expected": 13252},
    {"n": 91, "expected": 21533},
    {"n": 757, "expected": 2725885},
    {"n": 1000, "expected": 10804657},
]

for i, testcase in enumerate(testcases):
    output = s.punishmentNumber(testcase["n"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")   