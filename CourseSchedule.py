from typing import List
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Time Complexity : O(V+E)
Space Complexity: O(V+E)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we need to crate a hash map to store the course:prereq pairs 
        preMap = {i : [] for i in range(numCourses)}

        for course, preReq in prerequisites:
            preMap[course].append(preReq)
        
        visitedSet = set()

        def dfs(course):

            if course in visitedSet:
                return False

            if preMap[course] == []:
                return True
            
            visitedSet.add(course)
            for crs in preMap[course]:
                if not dfs(crs): return False
            
            visitedSet.remove(course)
            preMap[course] = []
            return True 
        
        # we have to do this to consider nodes that are not connected, for example: 1 -> 2, 3 -> 4
        for crs in range(0, numCourses):
            if not dfs(crs): return False
        return True

        
solution = Solution()
numCourses = 2
prerequisites = [[1,0]]
solution.canFinish(numCourses, prerequisites)