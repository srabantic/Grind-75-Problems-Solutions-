from typing import Optional
"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Notes:
Time Complexity : O(n)
Space Complexity : O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elementsList = []

        def inOnderTraversal(node):
            nonlocal elementsList
            if not node:
                return 
            inOnderTraversal(node.left)
            elementsList.append(node.val)
            inOnderTraversal(node.right)
        
        inOnderTraversal(root)

        if elementsList:
            return elementsList[k-1]

solution = Solution()
root = TreeNode(3)
t1 = TreeNode(1)
t2 = TreeNode(4)
t3 = TreeNode(2)
root.left = t1 
root.right = t2
t1.right = t3
k = 1
print(solution.kthSmallest(root, k))

root1 = TreeNode(5)
t4 = TreeNode(3)
t5 = TreeNode(6)
t6 = TreeNode(2)
t7 = TreeNode(9)
t8 = TreeNode(1)
root1.left = t4
root1.right = t5
t4.left = t6
t4.right = t7
t6.left = t8
k1 = 3
print(solution.kthSmallest(root1, k1))