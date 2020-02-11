class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while (i>0) and (nums[i-1]>=nums[i]):
            i -= 1

        if i == 0:
            nums.sort()
        else:
            # 从后往前找到第一个减小的数
            for j in range(len(nums)-1, i-1, -1):
                # 找到第一个大于次数的数进行调换
                if nums[j]>nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    # Python中可以连续赋值
                    nums[i:] = nums[i:][::-1]
                    # 注意要结束函数
                    return None

if __name__ == "__main__":
    # Test Case
    nums = [2,2,0,4,3,1]

    sol = Solution()
    sol.nextPermutation(nums)
    print(nums)