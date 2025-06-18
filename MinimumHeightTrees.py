from typing import List, DefaultDict, Deque
"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Notes: 
A tree will have minimum height when we pick the center notes as the root of the tree.
For trees with even number of nodes, we can have 2 center nodes from which leave and root will be equidistant
For trees with odd number of nodes, we can have 1 center node from which the leave and root will be equidistant
We will remove the leave nodes until we are left with at most 2 nodes in our tree and those 
2 nodes will be the roots of our MHT's.

Time Complexity : O(Nodes + Edges)
Space Complexity : O(Nodes + Edges)
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjListDict = DefaultDict(list)

        if n == 1:
            return [0]

        for n1, n2 in edges:
            adjListDict[n1].append(n2)
            adjListDict[n2].append(n1)

        edge_count = {}
        leaves = Deque()

        for src, neighbours in adjListDict.items():
            if len(neighbours) == 1:
                leaves.append(src)
            edge_count[src] = len(neighbours)
        
        while leaves:
            if (n <= 2):
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adjListDict[node]:
                    edge_count[nei] -= 1
                    if (edge_count[nei] == 1):
                        leaves.append(nei)

solution = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]
print(solution.findMinHeightTrees(n,  edges))

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
print(solution.findMinHeightTrees(n, edges))
