import heapq
from typing import List
"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Note:
    In python we can convert a min heap to max heap using heapq, by 
    converting all values to negetive, so that the most negetive value would 
    be at the top, henc that is the largest positive value.
    Alg:
        1. calculate the distance to the origin for each points and store them in a list, 
            since x2 and y2 are 0, the formula becomes sqrt(x^2 + y^2)
        2. we store it as follows [distance, x, y]
        3. call heapify to contruct the heap 
        4. then based on how many element we need to return (k), we pop from the heap and return the result array.

    Time Complexity:
        - to calculate the distance and put them into the array takes O(n)
        - heaplify takes O(n)
        - poping from the heap and maintain the heap property again O(log n)
        - poping k elements and inserting into the array takes O(k)

        All together, O(n)+O(n)+O(k⋅logn) = O(n+k⋅logn)
    
        - We can also use python's lambda sort to solve this

"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)
        result = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -=1
        return result

solution = Solution()

points = [[3,3],[5,-1],[-2,4]]
k = 2
points1 = [[1,3],[-2,2]]
k1 = 1
print(solution.kClosest(points, k))
print(solution.kClosest(points1, k1))