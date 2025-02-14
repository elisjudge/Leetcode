from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversalRec(self, root: Optional[TreeNode]) -> list[int]:
        """ Recursive Solution"""
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return(res)
    
    def inorderTraversalIter(self, root: Optional[TreeNode]) -> list[int]:
        """ Iterative Solution"""
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res

    

s = Solution()

#       1  
#      / \
#         2
#        / \
#       3    

tree1root = TreeNode(val=1)
tree1node1 = TreeNode(val=2)
tree1node2 = TreeNode(val=3)
tree1root.right = tree1node1
tree1node1.left = tree1node2

print(s.inorderTraversalRec(tree1root)) # [1, 3, 2]
print(s.inorderTraversalIter(tree1root)) # [1, 3, 2]

#        1  
#      /   \
#     2     5
#    / \   / \
#   3   4 6   7 

tree2node1 = TreeNode(val=1)
tree2node2 = TreeNode(val=2)
tree2node3 = TreeNode(val=3)
tree2node4 = TreeNode(val=4)
tree2node5 = TreeNode(val=5)
tree2node6 = TreeNode(val=6)
tree2node7 = TreeNode(val=7)

tree2root = tree2node1
tree2root.left = tree2node2
tree2root.left.left = tree2node3
tree2root.left.right = tree2node4
tree2root.right = tree2node5
tree2root.right.left = tree2node6
tree2root.right.right = tree2node7

print(s.inorderTraversalRec(tree2root)) # [3, 2, 4, 1, 6, 5, 7]
print(s.inorderTraversalIter(tree2root)) # [3, 2, 4, 1, 6, 5, 7]

