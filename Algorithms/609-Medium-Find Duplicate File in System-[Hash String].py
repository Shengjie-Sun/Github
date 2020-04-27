class Solution:
    def findDuplicate(self, paths):
        dic = dict()
        res = []
        for path in paths:
            parts = path.split(" ")
            files = parts[1:]
            folder = parts[0]

            for file in files:
                name, content = file.split("(")
                if content in dic:
                    dic[content].append(folder+"/"+name)
                else:
                    dic[content] = [folder+"/"+name]
            
        for value in dic.values():
            if len(value)>1:
                res.append(value)

        return res


if __name__ == "__main__":
    # Test Case
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

    sol = Solution()
    print(sol.findDuplicate(paths))