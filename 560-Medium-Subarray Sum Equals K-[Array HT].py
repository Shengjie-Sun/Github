import collections

class Solution1:
    def subarraySum(self, nums, k: int) -> int:
        N = len(nums)
        count = 0
        
        SUM = [0]*(N+1)
        for i, num in enumerate(nums):
            SUM[i+1] = SUM[i] + num

        for i in range(N+1):
            for j in range(i+1, N+1):
                if SUM[j]-SUM[i] == k:
                    count += 1
        
        return count

class Solution2:
    def subarraySum(self, nums, k: int) -> int:
        N = len(nums)
        count = 0
        
        for i in range(N):
            SUM = 0
            for j in range(i, N):
                SUM += nums[j]
                if SUM == k:
                    count += 1
        
        return count

class Solution3:
    def subarraySum(self, nums, k: int) -> int:
        
        dic = {0:1}
        SUM = 0
        count = 0
        
        for num in nums:
            SUM += num
            # SUM[j] - SUM[i] = K
            extra = SUM - k
            if extra in dic:
                count += dic[extra]
            if SUM in dic:
                dic[SUM]+=1
            else:
                dic[SUM]=1

        return count


if __name__ == "__main__":

    # Test Case
    nums = [1,1,1,1,1,1]
    k = 3
    
    sol = Solution1()
    print(sol.subarraySum(nums, k))