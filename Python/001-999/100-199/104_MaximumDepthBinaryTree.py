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

def print_tree(tree, level=0, prefix="root"):
    print(f"{level * '  '}{prefix:5s}: val={tree.val}")
    if tree.left:
        print_tree(tree.left, level + 1, "left")
    if tree.right:
        print_tree(tree.right, level + 1, "right")

def convert_tree_to_list(tree: Optional[TreeNode], output=None, is_root=False):
    if output is None:
        output = []
    if tree is None:
        return output
    if is_root:
        output.append(tree.val)
    if tree.left:
        output.append(tree.left.val)
    if tree.right:
        output.append(tree.right.val)

    if tree.left:
        output = convert_tree_to_list(tree.left, output)
    if tree.right:
        output = convert_tree_to_list(tree.right, output)

    return output            

class Solution:
    def maxDepthDFSR(self, root: Optional[TreeNode]) -> int:
        """ Uses Depth First Search with Recursion O(n) time, O(n) memory """
        if not root:
            return 0
        
        return 1 + max(self.maxDepthDFSR(root.left), self.maxDepthDFSR(root.right))
    
    def maxDepthDFSI(self, root: Optional[TreeNode]) -> int:
        """ Uses Depth First Search with Iteration O(n) time, O(n) memory """
        stack = [(root, 1)]
        result = 0

        while stack:
            node, depth = stack.pop()

            if node:
                result = max(result, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return result
    
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        """ Uses Breadth First Search O(n) time, O(n) memory"""
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

s = Solution()

testCases = [
    {"root": [3,9,20,None,None,15,7], "expected": 3},
    {"root": [1,None,2], "expected": 2}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    outputDFSR = s.maxDepthDFSR(root)
    outputDFSI = s.maxDepthDFSI(root)
    outputBFS = s.maxDepthBFS(root)
    
    if outputDFSR == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result(DFSR): {outputDFSR}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result(DFSR): {outputDFSR}")

    if outputDFSI == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result(DFSI): {outputDFSI}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result(DFSI): {outputDFSI}")

    if outputBFS == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result(BFS): {outputBFS}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result(BFS): {outputBFS}")
