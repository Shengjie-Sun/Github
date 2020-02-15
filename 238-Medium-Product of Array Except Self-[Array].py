class Solution1:
    def productExceptSelf(self, nums):
        
        N = len(nums)
        
        L, R, result = [1]*N, [1]*N, [None]*N
        
        for i in range(1, N):
            L[i] = L[i-1]*nums[i-1]
        
        for i in range(N-2, -1, -1):
            R[i] = R[i+1]*nums[i+1]
            
        for i in range(N):
            result[i] = L[i]*R[i]
            
        return result

class Solution2:
    def productExceptSelf(self, nums):
        
        N = len(nums)
        result = [1]*N
        
        for i in range(1, N):
            result[i] = result[i-1]*nums[i-1]
        
        R = 1
        for i in reversed(range(N)):
            result[i] *= R
            R *= nums[i]
            
        return result

class Solution3:
    def productExceptSelf(self, nums):
        
        N = len(nums)
        result = [None]*N
        
        L = 1
        for i in range(N):
            result[i] = L
            L *= nums[i]
        
        R = 1
        for i in reversed(range(N)):
            result[i] *= R
            R *= nums[i]
            
        return result

if __name__ == "__main__":
    # Test Case
    nums = [1,2,3,4]

    sol = Solution2()
    print(sol.productExceptSelf(nums))