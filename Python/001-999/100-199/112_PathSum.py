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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def dfs(node, target):
            if node is None:
                return False

            if node.left is None and node.right is None:
                return node.val == target
            
            target -= node.val
            return (dfs(node.left, target) or dfs(node.right, target))
        
        return dfs(root, targetSum)

s = Solution()

testCases = [
    {"root": [1,2], "targetSum": 1, "expected": False},
    {"root": [5,4,8,11,None,13,4,7,2,None,None,None,1], "targetSum": 22, "expected": True},
    {"root": [1,2,3], "targetSum": 5, "expected": False},
    {"root": [], "targetSum": 0, "expected": False}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    output = s.hasPathSum(root, testcase["targetSum"])
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result (DFS): {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result (DFS): {output}")


    