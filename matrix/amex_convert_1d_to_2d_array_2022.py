"""
Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
"""

class Solution(object):
    def construct_2d_array(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m*n != len(original):
            return []

        start = 0
        end = start+n

        output = []
        for i in range(m):
            output.append(original[start:end])
            start = end
            end += n
        return output