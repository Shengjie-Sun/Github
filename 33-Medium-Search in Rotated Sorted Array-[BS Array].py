class Solution1:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        
        if target>nums[0]:
            for i, num in enumerate(nums):
                if num > target:
                    return -1
                elif num==target:
                    return i
            return -1
        elif target<nums[0]:
            for i in reversed(range(len(nums))):
                if nums[i] < target:
                    return -1
                elif nums[i]==target:
                    return i
            return -1
        else:
            return 0

class Solution2:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums)-1
        if nums[l] == target: return l
        if nums[r] == target: return r
        
        while l <= r:
            mid = (r + l) // 2
            
            if nums[mid] == target:
                return mid
            
            # 
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # nums[l] > nums[mid]
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

if __name__ == "__main__":
    # Test Case
    nums = [4,5,6,7,0,1,2]
    target = 0

    sol = Solution2()
    print(sol.search(nums, target))