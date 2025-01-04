class Solution:
    def __init__(self) -> None:
        pass

    def calPoints(self, operations: list[str]) -> int:

        def is_integer(character):
            try:
                int(character)
                return True
            except ValueError:
                return False

        stack = []

        for operation in operations:
            if is_integer(operation):
                stack.append(int(operation))

            if operation == "C":
                stack.pop()

            if operation == "D":
                stack.append(stack[-1] * 2)

            if operation == "+":
                stack.append(stack[-2] + stack[-1])

        return sum(stack)


ops1 = ["5","2","C","D","+"]
ops2 = ["5","-2","4","C","D","9","+","+"]
ops3 = ["1","C"]

s = Solution()
print(s.calPoints(ops1))
print(s.calPoints(ops2))
print(s.calPoints(ops3))