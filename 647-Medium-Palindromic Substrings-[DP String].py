class Solution:
    def countSubstrings(self, s):
        N = len(s)
        states = [[0]*N for _ in range(N)]
        
        for offset in range(N):
            for i in range(N-offset):
                j = i+offset
                if offset==0:
                    states[i][j] = 1
                elif offset == 1:
                    states[i][j] = s[i]==s[j]
                else:
                    states[i][j] = states[i+1][j-1]*(s[i]==s[j])
        return states
                

if __name__ == "__main__":
    # Test Case
    s="abbcbcc"

    sol = Solution()
    states = sol.countSubstrings(s)
    for line in states:
        print(" ".join(format(state, '3') for state in line))