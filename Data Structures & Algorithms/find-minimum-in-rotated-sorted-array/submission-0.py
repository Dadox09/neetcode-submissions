class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2    
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
        return nums[lo]

        #[4,5,6,7,8,1,2,3]
        #[1,2,3,4]  
        #[]


    
        