class Solution:
    def checkPossibility(self, nums):
        if not nums or len(nums)<3: 
            return True
        N = len(nums)
        # dum if not needed actually
        dum = []
        for i in range(N-1):
            if nums[i] > nums[i+1]:
                dum.append((i, nums[i]))
        if len(dum)>1:
            return False
        elif len(dum)==1:
            index = dum[0][0]
            if 0 < index < N-2:
                return nums[index+2]>nums[index] or nums[index+1]>nums[index-1]
        return True
        
                

if __name__ == "__main__":
    # Test Case
    nums = [2,3,3,2,4] # change the number decreased
    nums = [-1,4,2,3]  # change the number before number decreased

    sol = Solution()
    print(sol.checkPossibility(nums))