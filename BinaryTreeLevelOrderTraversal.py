from collections import deque
from typing import Optional, List
"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
Note:
    -> We use a deque(double ended queue) since we can append and pop on both sides of the queue 
    -> we first check is root node is null, if not we add it to the queue 
    -> when we run a while loop until the queue is empty
    -> we define a list to hid the vals for each level 
    -> we ran a for loop for the length of the queue
    -> we pop the node from the begininf the queue and check if it has 
        a left or right child. 
    -> if yes, then we add them to the queue and repeat again 
    -> at the end, add the level to the result list. 
Time Complexity: O(n)
Space Complexity : O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []

        if not root:
            return result
        
        queue.append(root)
        while queue:
            level = []
            for i in range (0, len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if level:
                result.append(level)
        return result
                

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
print(solution.levelOrder(root))

    
        