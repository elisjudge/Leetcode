class Solution:
    def lengthOfLastWordCheat(self, s: str) -> int:
        """
        Easy cheating solution using str.split()
        """
        strList = s.split()
        return len(strList[-1])

    def lengthOfLastWord(self, s: str) -> int:
        """
        This solution will start from the end of the string 
        and begin counting the number of characters in a word.
        Any whitespaces will be ignored before beginning the count.
        As soon as a subsequent whitespace is hit, or the end of the string
        is reached, then the length of the word will be returned.
        Length of word will be done by counting characters.
        Time complexirty = o(n), memory complexity = o(1)
        """

        i, length = len(s)-1, 0

        while s[i] == " ":
            i-= 1
        
        while i >= 0 and s[i] != " ":
            length +=1
            i-=1
        return length
        
        
s = Solution()

testcases = [
    {"s": "Hello World", "expected": 5},
    {"s": "   fly me   to   the moon  ", "expected": 4},
    {"s": "luffy is still joyboy", "expected": 6}
]

for i, testcase in enumerate(testcases):
    output1 = s.lengthOfLastWordCheat(testcase["s"])
    output2 = s.lengthOfLastWord(testcase["s"])

    if output1 == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (Cheating): {output1}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (Cheating): {output1}")
    
    if output2 == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (Proper): {output2}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (Proper): {output2}")
