class Solution:
    def __init__(self) -> None:
        pass

    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")":"(", "}":"{", "]":"[" }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
                
        return not stack


s1 = "()"
s2 = "()[]{}"
s3 = "(]"

s=Solution()

print(s.isValid(s1))
print(s.isValid(s2))
print(s.isValid(s3))

        