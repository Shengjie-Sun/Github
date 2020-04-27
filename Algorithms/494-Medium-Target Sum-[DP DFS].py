from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums, S):
        N = len(nums)
        prev = defaultdict(int)
        prev[nums[0]] += 1; prev[-nums[0]] += 1
        
        for i in range(1, N):
            curr = defaultdict(int)
            for value, count in prev.items():
                curr[value-nums[i]] += count
                curr[value+nums[i]] += count
            prev = curr
        return prev
                

if __name__ == "__main__":
    # Test Case
    nums = [1,1,1]
    S = 3

    sol = Solution()
    states = sol.findTargetSumWays(nums, S)
    print(states)