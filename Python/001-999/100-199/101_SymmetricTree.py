from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(values: list) -> TreeNode:
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    nodes = [root]
    for node in nodes:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            nodes.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            nodes.append(node.right)
    return root

class Solution:
    def isSymmetricDFS(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        
        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            if ((node1 is None or node2 is None) or
                node1.val != node2.val):
                return False
            
            return (dfs(node1.left, node2.right) and dfs(node1.right, node2.left))
        
        return dfs(root.left, root.right)
    
    def isSymmetricBFS(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root.left, root.right)])
        while q:
            left, right = q.popleft()

            if left is None and right is None:
                continue

            if ((left is None or right is None) or
                left.val != right.val):
                return False

            q.append((left.left, right.right))
            q.append((left.right, right.left))

        return True    

s = Solution()

testCases = [
    {"root": [1,2,2,3,4,4,3], "expected": True},
    {"root": [1,2,2,None,3,None,3], "expected": False},
    {"root": [1], "expected": True}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    outputBFS = s.isSymmetricBFS(root)
    outputDFS = s.isSymmetricDFS(root)
    
    if outputDFS == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (DFS): {outputDFS}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (DFS): {outputDFS}")
    
    if outputBFS == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (BFS): {outputBFS}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (BFS): {outputBFS}")