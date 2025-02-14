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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

s = Solution()

test_trees = [
    { "tree": [4,2,7,1,3,6,9], "expected": [4,7,2,9,6,3,1] },
    { "tree": [2,1,3], "expected": [2,3,1] },
    { "tree": [], "expected": [] },
]

for i, tree in enumerate(test_trees):
    t = construct_tree(tree["tree"])
    t = s.invertTree(t)
    output = convert_tree_to_list(tree=t, is_root=True)
    if ','.join(str(x) for x in output) == ','.join(str(x) for x in tree["expected"]):
        print(f'Test {i+1}: Passed. Original: {tree["tree"]}, Expected: {tree["expected"]}, Output: {output}')
    else:
        print(f'Test {i+1}: Failed. Original: {tree["tree"]}, Expected: {tree["expected"]}, Output: {output}')

