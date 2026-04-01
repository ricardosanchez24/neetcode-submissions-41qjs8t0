class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        leng = 0
        righ = len(matrix) - 1
        
        while leng <= righ:
            m = (righ + leng) // 2

            if target > matrix[m][-1]:
                leng = m + 1
            elif target < matrix[m][0]:
                righ = m - 1
            else: 
                break    
                    
        #m = (righ + leng) // 2
        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            medio = (r + l) // 2

            if matrix[m][medio] > target:
                r = medio - 1
            elif matrix[m][medio] < target:
                l = medio + 1
            else:
                return True    

        return False