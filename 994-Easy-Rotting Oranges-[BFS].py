class Solution:
    def orangesRotting(self, grid) -> int:
        if not grid:
            return 0
        N = len(grid)
        
        starts = set()
        fresh = set()
        
        H = [1, -1, 0, 0]
        V = [0, 0, 1, -1]
        
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 2:
                    starts.add((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        
        print(starts)
        print(fresh)
        # while fresh:

if __name__ == "__main__":
    # Test Case
    grid = [[2,1,1],[1,1,0],[0,1,1]]

    sol = Solution()
    print(sol.orangesRotting(grid))