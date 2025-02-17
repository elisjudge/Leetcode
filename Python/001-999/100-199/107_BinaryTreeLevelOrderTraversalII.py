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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        
        result = []
        q = deque([root])

        while q:
            level_nodes = []
            for _ in range(len(q)):
                node = q.popleft()
                level_nodes.append(node)
            
            level_vals = []
            for node in level_nodes:
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            result.append(level_vals)
        
        result.reverse()
        return result


s = Solution()

testCases = [
    {"root": [3,9,20,None,None,15,7], "expected": [[15,7],[9,20],[3]]},
    {"root": [1], "expected": [[1]]},
    {"root": [], "expected": []}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    output = s.levelOrderBottom(root)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
