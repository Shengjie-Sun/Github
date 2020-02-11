class Solution:
    def twoSum(self, numbers, target):
        if len(numbers) < 2:
            return None
        
        i, j = 0, len(numbers)-1
        cdt = numbers[i] + numbers[j]
        
        while i < j and cdt != target:
            if cdt > target:
                j -= 1
            elif cdt < target:
                i += 1
            cdt = numbers[i] + numbers[j]
            
        return [i+1, j+1]
                

if __name__ == "__main__":
    # Test Case
    numbers = [2,7,11,15]
    target = 9

    sol = Solution()
    print(sol.twoSum(numbers, target))