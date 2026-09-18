class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        total = 0

        while l < r:
            
            if maxL <= maxR:
                l += 1
                water = max(maxL - height[l], 0)
                total += water

                if height[l] > maxL:
                    maxL = height[l]
            
            else:
                r -= 1
                water = max(maxR - height[r], 0)
                total += water

                if height[r] > maxR:
                    maxR = height[r]

        return total