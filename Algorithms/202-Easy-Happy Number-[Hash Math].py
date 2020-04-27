class Solution:
    def isHappy(self, n):
        
        # 通过Hash Table检测Circle
        record = set()
        while n != 1:
            digits = [int(d) for d in str(n)]
            n = sum(d*d for d in digits)
            if n not in record:
                record.add(n)
            else:
                return False
            
        return True


if __name__ == "__main__":
    # Test Case
    n = 19

    sol = Solution()
    print(sol.isHappy(n))