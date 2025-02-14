class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)

        while b:
            without_carry = a ^ b
            carry = (a & b) << 1
            a, b = without_carry, carry
        
        return bin(a)[2:]


s = Solution()

testCases = [
    {"a": "11" , "b": "1", "expected": "100"},
    {"a": "1010", "b": "1011", "expected": "10101"}
]

for i, testcase in enumerate(testCases):
    output = s.addBinary(testcase["a"], testcase["b"])
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")