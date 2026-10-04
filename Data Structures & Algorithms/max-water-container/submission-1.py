class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo, hi = 0, len(heights) - 1
        max_area = float('-inf')
        while lo < hi:
            area = min(heights[lo], heights[hi]) * (hi - lo)
            max_area = max(area, max_area)
            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
        return max_area