class Solution:
    def maxArea(self, height):
        if not height:
            return 0
        
        area = 0
        l = 0
        r = len(height)-1
        
        while r>l:
            h = min(height[r], height[l])
            w = r-l
            area = max(area, h*w)
            # 两个指针从两端开始；
            # 如果左边小于右边，那左边所能达到的最大面积就是当前情况；
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return area
                

if __name__ == "__main__":
    # Test Case
    height = [1,8,6,2,5,4,8,3,7]

    sol = Solution()
    print(sol.maxArea(height))