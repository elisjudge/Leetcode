class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []

        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        
        return res

s = Solution()

testCases = [
    {"n": 3, "expected": ["1","2","Fizz"]},
    {"n": 5, "expected": ["1","2","Fizz","4","Buzz"]},
    {"n": 15, "expected": ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]}
]

for i, testcase in enumerate(testCases):
    output = s.fizzBuzz(testcase["n"])
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")