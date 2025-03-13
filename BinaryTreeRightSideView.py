from typing import List,Optional, Deque
"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

Notes: 
 We are using BFS, also known as the level order traversing here. 
 Time Complexity: O(n)
 Space Complexity: O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideView = []
        queue = Deque([root])

        while queue:
            rightSideNode = None
            for i in range(0, len(queue)):
                node = queue.popleft()
                if node:
                    rightSideNode = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSideNode:
                rightSideView.append(rightSideNode.val)

        return rightSideView

treeNode1 = TreeNode(1)
treeNode2 = TreeNode(2)
treeNode3 =  TreeNode(5)
treeNode4 = TreeNode(3)
treeNode5 = TreeNode(4)

treeNode1.left = treeNode2
treeNode1.right = treeNode4
treeNode2.right = treeNode5
treeNode4.right = treeNode5

solution = Solution()
print(solution.rightSideView(treeNode1))


                

