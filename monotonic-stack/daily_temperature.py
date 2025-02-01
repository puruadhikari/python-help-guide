"""
Given an array of integers temperatures represents the daily temperatures, return an array answer
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = []
        result = [-1] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i

            stack.append(i)

        for idx in range(len(temperatures)):
            if result[idx] != -1:
                output.append(result[idx] - idx)
            else:
                output.append(0)

        return output

temps = [73,74,75,71,69,72,76,73]
sol = Solution()

print(sol.dailyTemperatures(temps))