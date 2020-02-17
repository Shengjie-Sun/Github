class Solution:
    def merge(self, intervals):
        if not intervals:
            return None
        
        intervals.sort(key= lambda x:x[0])
        result = [intervals[0]]
        
        for l, r in intervals[1:]:
            pre_l, pre_r = result[-1]
            
            if l > pre_r:
                result.append([l,r])
            elif r >= pre_r:
                result[-1][1] = r 
                
        return result

if __name__ == "__main__":
    # Test Case
    intervals = [[1,3],[2,6],[8,10],[15,18]]

    sol = Solution()
    print(sol.merge(intervals))