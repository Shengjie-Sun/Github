class Solution:
    def letterCombinations(self, digits):
        
        phone = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        
        def recursivor(combination, left_digits):
            if not left_digits:
                output.append(combination)
            else:
                for letter in phone[left_digits[0]]:
                    recursivor(combination+letter, left_digits[1:])

        output = []
        if digits:
            recursivor("", digits)
        return output


if __name__ == "__main__":
    # Test Case
    digits = "23"

    sol = Solution()
    print(sol.letterCombinations(digits))