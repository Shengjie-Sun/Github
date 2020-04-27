class Solution:
    def uniquePaths(self, m, n):
        curr = [1]*m
        for _ in range(n-1):
            for j in range(1,m):
                curr[j] += curr[j-1]
        return curr
                

if __name__ == "__main__":
    # Test Case
    m, n = 7, 3

    sol = Solution()
    states = sol.uniquePaths(m, n)
    print(" ".join(format(state, '3') for state in states))