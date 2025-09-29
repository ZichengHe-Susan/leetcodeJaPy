from typing import List
class Solution:
    def searchMatrix(self, matrix:List[List[int]], target:int) -> bool:
        left = 0
        m = len(matrix)
        n= len(matrix[0])
        right = m-1
        
        while left <= right:
            mid = (left + right)//2
            if matrix[mid][n-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left == m or matrix[left][0] > target or matrix[left][n-1] < target:
            return False

        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[left][mid] < target:         
                l = mid + 1
            else:
                r = mid - 1
        if l == n or matrix[left][l] != target:
            return False
        return True
            
            

if __name__ == "__main__":
    solver = Solution()

    m1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    t1 = 3
    e1 = True
    res1 = solver.searchMatrix(m1, t1)
    pass_fail1 = "PASS" if res1 == e1 else "FAIL"
    print(f"[{pass_fail1}] Test case 1 result: {res1}, Expected Result: {e1}")
