di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

class Solution:        
    # The first corrent version I have written "fast" but dirty.
    def numIslands_dfs_visited_ugly(self, grid):
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i, j):
            visited.add((i, j))
            for d in range(len(di)):
                ni, nj = i + di[d], j + dj[d]
                # Put the if condition here leads to redundancy.
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]=="1" and (ni, nj) not in visited:
                    dfs(ni, nj)
                else:
                    visited.add((ni, nj))
            return 1
        
        # The judge statement is a must becasue as long as dfs called, it returns 1.
        return sum([dfs(i, j) for i in range(n) for j in range(m) if (i, j) not in visited and grid[i][j]=="1"])

    def numIslands_dfs_visited_clean(self, grid):
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i, j):
            # Put the if condition here is suitable!
            if 0<=i<n and 0<=j<m and grid[i][j]=="1" and (i, j) not in visited:
                visited.add((i, j))
                for d in range(len(di)):
                    dfs(i+di[d], j+dj[d])
                return 1
            return 0
        
        return sum([dfs(i, j) for i in range(n) for j in range(m)])
    
    # Modified from Stefan Pochmann, changing the grid is not good but "map" make the codes lean.
    def numIslands_dfs_floodfill(self, gird):
        if not grid: return 0

        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if 0<=i<n and 0<=j<m and grid[i][j]=="1":
                grid[i][j]="0"
                list(map(dfs, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0

        return sum([dfs(i, j) for i in range(n) for j in range(m)])
    

        
if __name__ == "__main__":
    # Test Case
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    sol = Solution()
    print(sol.numIslands_dfs_visited_ugly(grid))
    