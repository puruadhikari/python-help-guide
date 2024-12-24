class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)

        sum_number = (n*(n+1))/2

        for items in matrix:
            if sum(items) != sum_number:
                return False
        return True

matrix1 =[[1,2,3],[3,1,2],[2,3,1]]
matrix2 =[[1,1,1],[1,2,3],[1,2,3]]

sol = Solution()
print(sol.checkValid(matrix2))