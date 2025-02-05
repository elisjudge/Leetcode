from collections import deque

from typing import Optional
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        if root.left is None and root.right is None:
            return [float(root.val)]
        res = []
        q = deque([root])
            
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr)
            
            val_sum = 0
            n_nodes_level = len(level)
            
            for node in level:
                val_sum += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
            res.append(val_sum/n_nodes_level)
        
        return res
        
s = Solution()

testCases = [
    {"root": [3,9,20,None,None,15,7], "expected": [3.00000,14.50000,11.00000]},
    {"root": [3,9,20,15,7], "expected": [3.00000,14.50000,11.00000]}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    output = s.averageOfLevels(root)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (BFS): {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (BFS): {output}")


    