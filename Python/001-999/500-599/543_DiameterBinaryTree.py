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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(curr):
            """ Returns Height of Tree """
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return res    



s = Solution()

testCases = [
    {"root": [1,2,3,4,5], "expected": 3},
    {"root": [1,2], "expected": 1}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    output = s.diameterOfBinaryTree(root)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
    
