from typing import List
"""
Given an array of meeting time intervals consisting of start and end times
[[s1, e1], [s2, e2], ....] (si < ei), determine if a person
could attend all meeting.

Example:
InputL intervals = [(0, 30), (5, 10), (15, 20)]
Output: False

Note:
    If we solve this problem using 2 loops, it will have a time complexity of O(n^2)
    If we use python's build in sorting(TimSort), we know that the time complexity of it is O(n log n)
    Lambda sorting:
        Python, lambda sorting refers to using a lambda function as the key for sorting a collection (like a list) using the sorted() function or the .sort() method. 
        A lambda function is an anonymous function (a function without a name) defined using the lambda keyword. It is commonly used for short operations that can be expressed in a single line.
        Syntax: sorted(iterable, key=lambda x: <expression>)
    Difference betweeb sort and sorted in python
        - sort is only used for lists, sort perfoms in place sorting and mutates the original list, reduces use of extrs memory, reduces space complexity.
        - sorted can be used for variety of iterals, lists, tuples, sets etc. It returns a new list, so does not mutate the original list and has a bigger space complexity.
        - However, both soting functions have a time complexity of O(n log n) - worst case.

"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_times = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(intervals)):
            i_a = intervals[i - 1]
            if (intervals[i].start < i_a.end):
                return False
        return True


i1 = Interval(0, 30)
i2 = Interval(5, 10)
i3 = Interval(15, 20)

i4 = Interval(31, 45)
i5 = Interval(50, 120)

intervals = [i1, i2, i3]
intervals1 = [i1, i4, i5]

solution = Solution()
print(solution.canAttendMeetings(intervals))
print(solution.canAttendMeetings(intervals1))
