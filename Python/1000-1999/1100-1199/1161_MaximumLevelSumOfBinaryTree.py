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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        max_sum = float('-inf')
        level = 1
        min_level = level

        while q:
            level_nodes = []
            level_sum = 0    
            for _ in range(len(q)):
                node = q.popleft()
                level_nodes.append(node)
            
            for node in level_nodes:
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                min_level = level

            level += 1    
            
        return min_level            


s = Solution()

testCases = [
    {"root": [1,7,0,7,-8,None,None], "expected": 2},
    {"root": [989,None,10250,98693,-89388,None,None,None,-32127], "expected": 2}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    output = s.maxLevelSum(root)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")