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

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        
        if not root:
            self.root = None
        elif not root.left and not root.right:
            self.root = TreeNode()
            self.values.add(0)
        else:
            self.root = self.repair(root, method="BFS")

    def find(self, target: int) -> bool:
        return target in self.values

    def repair(self, root, method="BFS"):
        """ 
        Repairs Binary Tree and records values. 
        Default method is BFS. Methods: "BFS", "DFS". 
        """
        if method == "BFS":
            q = deque([(root, 0)])  # node, val

            while q:
                level_nodes = [q.popleft() for _ in range(len(q))]
                for node, val in level_nodes:
                    node.val = val

                    self.values.add(val)
                    if node.left:
                        q.append((node.left, (2 * val + 1)))
                    
                    if node.right: 
                        q.append((node.right, (2 * val + 2)))
            return root

        elif method == "DFS":
            def dfs(node, val):
                if not node:
                    return None
                node.val = val
                self.values.add(val)

                node.left = dfs(node.left, (2 * val + 1))
                node.right = dfs(node.right, (2 * val + 2))
                return node

            return dfs(root, 0)
            

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

testCases = [
    {
        "calls": ["findElements", "find", "find"],
        "args": [[[-1,None,-1]],[1],[2]],
        "expected": [None, False, True],
    }
]

for i, testcase in enumerate(testCases):
    output = []
    for call, args in zip(testcase["calls"], testcase['args']):
        if call == "findElements":
            root = construct_tree(args[0]) 
            obj = FindElements(root)
            output.append(None)
        elif call == "find":
            target = args[0]
            output.append(obj.find(target))
    
    if output == testcase["expected"]:
        print(f"Test Case {i} Passed. Expected: {testcase['expected']}, Result: {output}")
    else:
        print(f"Test Case {i} Failed. Expected: {testcase['expected']}, Result: {output}")
    