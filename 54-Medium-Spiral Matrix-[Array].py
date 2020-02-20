class Solution1:
    def spiralOrder(self, matrix) -> list:
        if not matrix:
            return None
        
        result = []
        m, n = len(matrix), len(matrix[0])
        
        h = [1, 0, -1, 0]
        v = [0, 1, 0, -1]
        
        cur = [0, 0]
        idx = 0
        
        while len(result) < m*n:
            
            if 0<=cur[0]<m and 0<=cur[1]<n and matrix[cur[0]][cur[1]] != '#':
                result.append(matrix[cur[0]][cur[1]])
                matrix[cur[0]][cur[1]] = '#'
            else:
                cur = [cur[0]-v[idx], cur[1]-h[idx]]
                idx = (idx+1) % 4
            cur = [cur[0]+v[idx], cur[1]+h[idx]]
        
        return result

class Solution2():
    def spiralOrder(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

if __name__ == "__main__":

    # Test Case
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    
    sol = Solution2()
    print(sol.spiralOrder(matrix))