from typing import Optional
"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Note:
    For each recursive call, for a left subtree, we update the right boundary and
    for a right subtree, we update the left boundary.
    This problem is following dfs approach, where we go down until the leaf node.

Time complexity: 
    Since we visit each node in the tree one time, O(n)
Space complecity:
    O(h), where h is the height of the tree, since we need to store that many recursive call stack.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True 
            
            if not (node.val > left and node.val < right):
                return False 
            
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
    
        return valid(root, float('-inf'), float('inf'))


solution = Solution()
root = TreeNode(2)
t1 = TreeNode(1)
t2 = TreeNode(3)
root.left = t1
root.right = t2
solution.isValidBST(root)