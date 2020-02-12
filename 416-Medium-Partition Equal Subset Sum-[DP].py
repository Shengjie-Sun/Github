class Solution1:
    def canPartition(self, nums):
        if sum(nums) % 2 == 1:
            return False
        else:
            S = sum(nums)//2
        
        states = [[0]*(S+1) for _ in range(len(nums))]
        
        for i, num in enumerate(nums):
            for j in range(S+1):
                if num <= S:
                    states[i][num] = 1
                if i and states[i-1][j] + (states[i-1][j-nums[i]] if j-nums[i]>=0 else 0):
                    states[i][j] = 1
        return states

class Solution2:
    def canPartition(self, nums):
        if sum(nums) & 1 == 1:
            return False
        else:
            S = sum(nums)//2
        
        states = [True]+[False]*S
        
        for num in nums:
            # 这里是个小技巧，将状态在nums上的维度压缩了，为此更新时候需从状态的末尾进行更新
            for j in range(S, -1, -1):
                states[j] = states[j] or (states[j-num] if j-num>=0 else False)
        return states  

if __name__ == "__main__":
    # Test Case
    nums = [2, 2, 3, 5]

    sol = Solution1()
    states = sol.canPartition(nums)
    print(states)