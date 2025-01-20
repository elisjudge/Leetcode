import random

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

ANSWER = 0

def generate_random_int(n: int) -> int:
    return random.randint(1, n)

def guess(num: int) -> int:
    if num > ANSWER:
        return -1
    elif num < ANSWER:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while True:
            m = (l + r) //  2
            res = guess(m)
            if res > 0:
                l = m+1
            elif res < 0:
                r = m-1
            else:
                return m
            
s= Solution()

testcases = [
    {"n": 10},
    {"n": 1},
    {"n": 2}, 
    {"n": 23},
    {"n": 90}
]

for i, testcase in enumerate(testcases):
    
    ANSWER = generate_random_int(testcase["n"])
    testcase["expected"] = ANSWER

    output = s.guessNumber(testcase["n"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")    