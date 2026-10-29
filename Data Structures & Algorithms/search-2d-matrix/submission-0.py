class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr,rr = 0, len(matrix) - 1
        while lr <= rr:
            mr = (lr + rr) // 2
            if matrix[mr][-1] < target:
                lr = mr + 1
            elif matrix[mr][0] > target:
                rr = mr - 1
            else:
                row = matrix[mr]
                l,r = 0,len(row)-1
                while l <= r:
                    mid = ( l + r ) // 2
                    if row[mid] < target:
                        l = mid + 1
                    elif row[mid] > target:
                        r = mid - 1
                    else:
                        return True
                return False
        return False