class Solution:
    def trap(self, height: List[int]) -> int:
        # water trapped over an array depends on the bounding boxes created by left and right side

        left_max = [0]*len(height)
        right_max = [0] *len(height)

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
        res = 0

        for i in range(len(height) -2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
            water_trapped = min(left_max[i], right_max[i]) - height[i]
            if water_trapped > 0:
                res += water_trapped

        
  
        return res

