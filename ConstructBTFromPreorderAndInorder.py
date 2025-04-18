from typing import Optional, List
"""
Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same tree, construct 
and return the binary tree.

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hashmap = {}
        self.pre_index = 0
        for indx, val in enumerate(inorder):
            inorder_hashmap[val] = indx
        
        def dfs(l, r):
            if l > r:
                return None
            
            root_value = preorder[self.pre_index]
            root = TreeNode(root_value)
            self.pre_index += 1
            mid = inorder_hashmap[root_value]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root 
        
        return(dfs(0, len(inorder) - 1))


            
preorder = [3, 4, 2, 1, 5, 6, 7]
inorder = [2, 4, 1, 3, 6, 5, 7]

solution = Solution()
solution.buildTree(preorder, inorder)

