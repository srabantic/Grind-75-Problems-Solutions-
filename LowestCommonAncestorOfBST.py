"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Input: root = [2,1], p = 2, q = 1
Output: 2

Note: LCA Definition: The lowest common ancestor is a node for which p & q will be decendents 
of the node.
BST: left child is always smaller than the root
    right child is always bigger than the root 
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current = root
        while current is not None:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                print(current.val)
                return current
        

root = TreeNode(6)
treeNode1 = TreeNode(2)
treeNode2 = TreeNode(8)
treeNode3 = TreeNode(0)
treeNode4 = TreeNode(4)
treeNode5 = TreeNode(3)
treeNode6 = TreeNode(5)
treeNode7 = TreeNode(7)
treeNode8 = TreeNode(9)
treeNode9 = TreeNode(None)
treeNode10 = TreeNode(None)

root.left = treeNode1
root.right = treeNode2
treeNode1.left = treeNode3
treeNode1.right = treeNode4
treeNode2.left = treeNode7
treeNode2.right = treeNode8
treeNode3.left = treeNode9
treeNode3.right = treeNode10
treeNode4.left = treeNode5
treeNode4.right = treeNode6

solution = Solution()
print(solution.lowestCommonAncestor(root, treeNode1, treeNode4))
print(solution.lowestCommonAncestor(root, treeNode7, treeNode8))
print(solution.lowestCommonAncestor(root, root, treeNode4))
