class Solution:
    def maximumSwap(self, num):
        num_str = str(num)
        result = [digit for digit in num_str]
        index = [(digit, i) for i, digit in enumerate(num_str)]
        for i, digit in enumerate(sorted(result, reverse=True)):
            if result[i] != digit:
                idx = max(tle[1] for tle in index if tle[0] == digit)
                result[idx] = result[i]
                result[i] = digit
                break
        return int(''.join(result))
        
                

if __name__ == "__main__":
    # Test Case
    num = 98368

    sol = Solution()
    print(sol.maximumSwap(num))