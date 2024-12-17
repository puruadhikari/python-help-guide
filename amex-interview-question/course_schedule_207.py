"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

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
"""
from collections import deque


class Solution(object):
    def can_finish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {}

        for index in range(numCourses):
            graph[index] = []

        pre_req_list = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            pre_req_list[course] += 1

        queue = deque()

        for item in pre_req_list:
            if item == 0:
                queue.append(item)

        course_counter = 0

        while queue:
            current_course = queue.popleft()
            course_counter += 1
            for nodes in graph[current_course]:
                pre_req_list[nodes] -= 1
                if pre_req_list[nodes] == 0:
                    queue.append(nodes)

        return course_counter == numCourses