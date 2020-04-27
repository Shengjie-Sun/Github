# return sorted(nums)[-k]
class Solution:
    def findKthLargest(self, nums, k):
        
        idx = len(nums)-k
        l, r = 0, len(nums)-1

        cdt = nums[r]
        split, j = l, l
        
        while j < r:
            if nums[j] <= cdt:
                nums[split], nums[j] = nums[j], nums[split]
                split += 1
            j += 1
        nums[split], nums[r] = nums[r], nums[split]
        
        if split == idx:
            result = cdt
            return result
        elif split > idx:
            result = self.findKthLargest(nums[:split], k-(len(nums)-split))
        elif split < idx:
            result = self.findKthLargest(nums[split+1:], k)
        
        return result
                
                

if __name__ == "__main__":
    # Test Case
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4

    sol = Solution()
    print(sol.findKthLargest(nums, k))