class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

       for arr in matrix:
        l = 0
        r = len(arr) - 1

        while l <= r:
            medio = (r + l) // 2

            if arr[medio] == target:
                return True
            elif arr[medio] > target:
                r = medio - 1
            else:
                l = medio + 1

       return False                 