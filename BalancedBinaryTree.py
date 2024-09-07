"""
Given a binary tree, determine if it is 
height-balanced.

height-balanced : A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        self.balanced = True

        if root is None:
            return True
        
        def dfs(node):

            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if (abs(left_height - right_height) > 1):
                self.balanced = False

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.balanced
    
# Example
root = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)

root.left = t1
root.right = t2
t2.left = t3
t2.left = t4

solution = Solution()
print(solution.isBalanced(root))

root1 = TreeNode(1)
t5 = TreeNode(2)
t6 = TreeNode(2)
t7 = TreeNode(3)
t8 = TreeNode(3)
t9 = TreeNode(4)
t10 = TreeNode(4)

root1.left = t5
root1.right = t6
t5.left = t7
t5.right = t8
t7.left = t9
t7.right = t10

solution = Solution()
print(solution.isBalanced(root1))
