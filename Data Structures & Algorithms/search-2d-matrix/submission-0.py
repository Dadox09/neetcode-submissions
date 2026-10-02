class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #i cant build an array m * n and then BS -> O(m*n log (m *n))
        #my idea: in a for loop i iterate through ith-row and every loop i do BS on that row
        #i think it is O(m log (n))
        #cant think a solution O(log (m*n))...

        m, n = len(matrix) , len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            current_val = matrix[mid // n][mid % n] #[quante volte mid sta in n][quanto sfora in n]
            if target > current_val:
                l = mid + 1
            elif target < current_val:
                r = mid - 1
            else:
                return True
        return False
            
