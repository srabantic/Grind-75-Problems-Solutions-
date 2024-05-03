'''
Given the root of a binary tree, invert the tree, and return its root.
Example:
  Input: root = [4,2,7,1,3,6,9]
  Output: [4,7,2,9,6,3,1]

# Time Complexity O(N) - because we would need to go through each node of the tree 
'''
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
  if root is None:
    return root 
    
  root.left, root.right = root.right, root.left 
  self.invertTree(root.left)
  self.invertTree(root.right)
  return root
