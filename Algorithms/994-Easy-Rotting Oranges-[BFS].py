import collections
class Solution:
    def orangesRotting(self, grid) -> int:
        R, C = len(grid), len(grid[0])
        
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))
        
        # 好方法！
        def neighbours(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr, nc)
                    
        depth = 0
        while queue:
            r, c, depth = queue.popleft()
            for nr, nc in neighbours(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, depth+1))
        
        if any(1 in row for row in grid):
            return -1
        
        return depth

if __name__ == "__main__":
    # Test Case
    grid = [[2,1,1],[1,1,0],[0,1,1]]

    sol = Solution()
    print(sol.orangesRotting(grid))