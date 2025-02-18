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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        result = []
        q = deque([root])
        level = 0
        while q:
            level_nodes = [q.popleft() for _ in range(len(q))]
            
            for i in range(len(level_nodes)):
                if level_nodes[i].left:
                    q.append(level_nodes[i].left)    
                if level_nodes[i].right:
                    q.append(level_nodes[i].right)    
                level_nodes[i] = level_nodes[i].val

            if level % 2 != 0:
                level_nodes.reverse()

            result.append(level_nodes)
            level += 1

        return result


s = Solution()

testCases = [
    {"root": [1,2,3,4,None,None,5], "expected": [[1],[3,2],[4,5]]},
    {"root": [3,9,20,None,None,15,7], "expected": [[3],[20,9],[15,7]]},
    {"root": [1], "expected": [[1]]},
    {"root": [], "expected": []}
]

for i, testcase in enumerate(testCases):
    root = construct_tree(testcase["root"])
    output = s.zigzagLevelOrder(root)
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")