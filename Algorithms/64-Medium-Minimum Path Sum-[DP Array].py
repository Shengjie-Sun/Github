class Solution:
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        curr = grid[0].copy()
        for j in range(1, m):
            curr[j]+=curr[j-1]

        for i in range(1,n):
            for j in range(m):
                curr[j] = grid[i][j] + (min(curr[j], curr[j-1]) if j>0 else curr[j])
        return curr

if __name__ == "__main__":
    # Test Case
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]

    sol = Solution()
    states = sol.minPathSum(grid)
    print(" ".join(format(state, '3') for state in states))