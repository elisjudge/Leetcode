class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        collision_stack = []

        for a in asteroids:
            if not collision_stack:
                collision_stack.append(a)
            else:
                if (collision_stack[-1] < 0 or a > 0):
                    collision_stack.append(a)
                else:
                    while collision_stack and collision_stack[-1] > 0 and abs(a) >= collision_stack[-1]:
                        prev_a = collision_stack.pop()
                        if abs(a) == prev_a:
                            break
                    if ((not collision_stack and abs(a) != prev_a) or
                        (collision_stack and collision_stack[-1] < 0 and abs(a) != prev_a)):
                            collision_stack.append(a)
        
        return collision_stack            

s= Solution()

testcases = [
    {"asteroids": [-2,-2,1,-1], "expected": [-2,-2]},
    {"asteroids": [-2,-2,1,-2], "expected": [-2,-2,-2]},
    {"asteroids": [5,10,-5], "expected": [5,10]},
    {"asteroids": [8,-8], "expected": []},
    {"asteroids": [10,2,-5], "expected": [10]}, 
]

for i, testcase in enumerate(testcases):
    output = s.asteroidCollision(testcase["asteroids"])

    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}") 