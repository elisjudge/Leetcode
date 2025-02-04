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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, leaves:list):
            if node.left is None and node.right is None:
                leaves.append(node.val)

            if node.left:
                leaves = dfs(node.left, leaves)

            if node.right:
                leaves = dfs(node.right, leaves)

            return leaves        

        leaves_1 = dfs(root1, [])
        leaves_2 = dfs(root2, [])

        return leaves_1 == leaves_2

s = Solution()

testCases = [
    {
        "root1": [3,5,1,6,2,9,8,None,None,7,4], 
        "root2": [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8],
        "expected": True},
    {
        "root1": [1,2,3], 
        "root2": [1,3,2], 
        "expected": False}
]

for i, testcase in enumerate(testCases):
    root1 = construct_tree(testcase["root1"])
    root2 = construct_tree(testcase["root2"])
    output = s.leafSimilar(root1, root2)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")