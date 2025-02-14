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
    def minDepthDFSR(self, root: Optional[TreeNode]) -> int:
        """ Uses Depth First Search with Recursion O(n) time, O(n) memory """
        if not root:
            return 0
        
        # If node has only one child, we can return the result for that path.
        if root.left is not None:
            return 1 + self.minDepthDFSR(root.left)
        if root.right is not None:
            return 1 + self.minDepthDFSR(root.right)

        # If node has both a left and right child, then we take the minimum
        return 1 + min(self.minDepthDFSR(root.left), self.minDepthDFSR(root.right))

    def minDepthBFS(self, root: Optional[TreeNode]) -> int:
        """ Uses Breadth First Search O(n) time, O(n) memory"""
        if root is None:
            return 0
        
        q = deque([(root, 1)])

        while len(q) > 0:
            node, depth = q.popleft()

            if node.left is None and node.right is None:
                return depth
            
            for child in [node.left, node.right]:
                if child is not None:
                    q.append((child, depth + 1))
            

s = Solution()

testCases = [
    {"root": [2,None,3,None,4,None,5,None,6], "expected": 5},
    {"root": [3,9,20,None,None,15,7], "expected": 2}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    outputDFSR = s.minDepthDFSR(root)
    outputBFS = s.minDepthBFS(root)
    
    if outputDFSR == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (DFSR): {outputDFSR}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (DFSR): {outputDFSR}")
    
    if outputBFS == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (BFS): {outputBFS}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (BFS): {outputBFS}")