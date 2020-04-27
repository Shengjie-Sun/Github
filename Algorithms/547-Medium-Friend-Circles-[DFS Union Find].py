class Solution1:
    def findCircleNum(self, M):
        if not M: return 0
        
        n, m = len(M), len(M[0])
        def dfs(i, j):
            if 0<=i<n and 0<=j<m and M[i][j]==1:
                M[i][j] = 0
                for _i in range(n):
                    dfs(_i, j)
                for _j in range(m):
                    dfs(i, _j)
                return 1
            return 0
        return sum(dfs(i, j) for i in range(n) for j in range(m) if j>=i)

class Solution2:
    # pay more attention to the symmetric 
    def findCircleNum(self, M):
        if not M: return 0
        
        N = len(M); seen = set()
        def dfs(i):
            seen.add(i)
            for j in range(N):
                if j not in seen and M[i][j]==1:
                    dfs(j)
            return 1

        return sum(dfs(i) for i in range(N) if i not in seen)

        

if __name__ == "__main__":
    # Test Case
    M = [[1,1,0],[1,1,0],[0,0,1]]

    sol = Solution1()
    print(sol.findCircleNum(M))