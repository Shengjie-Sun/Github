class Solution1:
    def longestPalindrome(self, s):
        N = len(s)
        states = [[0]*N for _ in range(N)]
        result = ""
        
        for diff in range(N):
            for i in range(N-diff):
                j = i+diff
                if j-i == 0:
                    states[i][j] = 1
                    result = s[i]
                elif j-i == 1:
                    if s[i] == s[j]:
                        states[i][j] = 1
                        result = s[i:j+1]
                elif s[i] == s[j] and states[i+1][j-1] > 0:
                    states[i][j] = 1
                    result = s[i:j+1]
        
        return result

class Solution2:
    def longestPalindrome(self, s):
        N = len(s)
        result = ""

        def findPalindrome(l, r):
            while 0<=l<=r<N and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(N):
            # max的新用法
            result = max(findPalindrome(i, i), findPalindrome(i, i+1), result, key=len)

        return result


if __name__ == "__main__":
    # Test Case
    s = "aaabaaaa"

    sol = Solution2()
    print(sol.longestPalindrome(s))
        
                