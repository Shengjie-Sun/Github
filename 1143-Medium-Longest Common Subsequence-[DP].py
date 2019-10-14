class Solution:
    def longestCommonSubsequence(self, text1, text2):
        L1, L2 = len(text1), len(text2)
        states = [[0]*(L2+1) for _ in range(L1+1)]
        for i in range(1, L1+1):
            for j in range(1, L2+1):
                states[i][j] = states[i-1][j-1] + 1 if text1[i-1]==text2[j-1] else max(states[i-1][j], states[i][j-1])
        return states[L1][L2]
        
                

if __name__ == "__main__":
    # Test Case
    text1 = "ace"
    text2 = "abcde"

    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))