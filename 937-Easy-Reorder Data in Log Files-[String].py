class Solution1:
    def reorderLogFiles(self, logs):
        letter = []
        digit = []
        for log in logs:
            parts = log.split(" ")
            try:
                int(parts[1])
                digit.append(parts)
            except:
                letter.append(parts)
        
        letter.sort(key=lambda x: x[1])
        logs.sort(key=lambda x: x[1])

        result = [" ".join(parts) for parts in letter + digit]

        return result

class Solution2:
    def reorderLogFiles(self, logs):
        def order(log):
            # 使用split的高级方法
            name, part = log.split(" ", 1)
            
            # Python中的isalpha()函数
            if part[0].isalpha():
                return (0, part, name)
            else:
                return (1, )
            
        # 使用sorted函数的高级方法
        return sorted(logs, key = order)

if __name__ == "__main__":
    # Test Case
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

    sol = Solution2()
    print(sol.reorderLogFiles(logs))