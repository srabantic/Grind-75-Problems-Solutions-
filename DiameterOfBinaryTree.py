from typing import Optional
"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

Notes: We will be follwoing the bottom up recursive approach (we only 
visit each node one time)

Height of a tree : 1 + Max(Left height, Right height)
Diameter of a tree: left height + right height 
Height of a null node is 0

"""
#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            height_left = dfs(root.left)
            height_right = dfs(root.right)

            self.res = max(self.res, height_left + height_right)
        
            return 1 + max(height_left, height_right)
        
        dfs(root)
        return self.res



root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
t3 = TreeNode(4)
t4 = TreeNode(5)

root.left = t1
root.right = t2
t1.left = t3
t1.right = t4

solution = Solution()
print(solution.diameterOfBinaryTree(root))

root2 = TreeNode(1)
t5 = TreeNode(2)

root2.left = t5
print(solution.diameterOfBinaryTree(root2))


