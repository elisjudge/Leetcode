class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        positive = (dividend < 0 and divisor < 0) or (dividend >= 0 and divisor > 0) 
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            multiple = 1
            temp_divisor = divisor
            while dividend > (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple

        if not positive:
            quotient = quotient - quotient - quotient
            return quotient if quotient > INT_MIN else INT_MIN

        return quotient if quotient < INT_MAX else INT_MAX

s = Solution()

testcases = [
    {"dividend": -2147483648, "divisor": -1, "expected": 2147483647},
    {"dividend": -1, "divisor": 1, "expected": -1},
    {"dividend": 10, "divisor": 3, "expected": 3},
    {"dividend": 7, "divisor": -3, "expected":-2}
]

for i, testcase in enumerate(testcases):
    output = s.divide(testcase["dividend"], testcase["divisor"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")