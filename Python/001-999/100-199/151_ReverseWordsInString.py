class Solution:
    def reverseWords(self, s: str) -> str:
        """ This modifies the string in place with O(1) memory"""
        # convert string to list of chars
        s = list(s)
        
        # First reverse list using two pointers
        l, r = 0, len(s) - 1
        while l <= r:
            s[r], s[l] = s[l], s[r]
            l += 1
            r -= 1
        
        # Next use two pointers to find each word boundary and then reverse the word
        l = r = 0

        while r < len(s): 
            while r < len(s) and s[r] == " ":
                r += 1 

            word_l = word_r = r
            while word_r < len(s) and s[word_r] != " ":
                word_r += 1

            # reverse word
            end = word_r 
            word_r -= 1
            while word_l <= word_r:
                s[word_r], s[word_l] = s[word_l], s[word_r]
                word_l += 1
                word_r -= 1

            # Shift word back to start and replace with spaces
            if r > l:
                for i in range(l, len(s) - (r - l)):
                    s[i] = s[i + (r - l)]
                for i in range(len(s) - (r - l), len(s)):
                    s[i] = " "
                end -= (r - l)

            l = end + 1
            r = l

        # Pop off any whitespace at end
        while True:
            if s[-1] == " ":
                s.pop()
            else:
                break

        return "".join(s)                

s = Solution()

testcases = [
    {
        "s": "  so        much white      space        ", 
        "expected": "space white much so"
    },
    {
        "s": "  hello world  ", 
        "expected": "world hello"
    },
    {
        "s": "a good   example", 
        "expected": "example good a"
    },
    {
        "s": "the sky is blue",
        "expected": "blue is sky the"
    },
]

for i, testcase in enumerate(testcases):
    output = s.reverseWords(testcase["s"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
    