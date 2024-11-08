from typing import Optional
"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.height = 0

        def dfs(root):
            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right) 

            self.height =  1 + max(left_height, right_height)
            return self.height
        
        dfs(root)
        return self.height


root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)

root.left = t1
root.right = t2
t2.left = t3
t2.right = t4 

solution = Solution()
print(solution.maxDepth(root))

root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)

root.left = t1
root.right = t2
t1.left = t3
t1.right = t4 

solution = Solution()
print(solution.maxDepth(root))

root1 = TreeNode(1)
t5 = TreeNode(2)
root1.left = t5

solution = Solution()
print(solution.maxDepth(root1))

root2 = TreeNode(1)
t6 = TreeNode(2)
t7 = TreeNode(4)
t8 = TreeNode(3)
t9 = TreeNode(5)

root2.left = t6
root2.right = t8
t6.left = t7
t8.right = t9

solution = Solution()
print(solution.maxDepth(root2))

