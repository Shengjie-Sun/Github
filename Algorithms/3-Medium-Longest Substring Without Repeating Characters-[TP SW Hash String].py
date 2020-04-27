class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        result = 0
        for i in range(1, N):
            for j in reversed(range(i)):
                sub = s[j:i+1]
                if len(set(sub)) == len(sub):
                    result = max(result, len(sub))
                else:
                    break
        return result

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        l = 0

        # 记录所有见过的元素的最近的index
        dic = dict()
        result = 1

        # [l, r]为当前的最大Substring
        for r in range(N):
            if s[r] not in dic:
                result = max(result, r-l+1)
            else:
                if dic[s[r]] >= l:
                    l = dic[s[r]] + 1
                else:
                    result = max(result, r-l+1)
            dic[s[r]] = r

        return result

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        l = 0

        dic = dict()
        result = 1

        for r in range(N):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            result = max(result, r-l+1)
            dic[s[r]] = r

        return result
                    

if __name__ == "__main__":
    # Test Case
    s = "aab"

    sol = Solution2()
    print(sol.lengthOfLongestSubstring(s))