class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        
        for i, n in enumerate(nums):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                if n + nums[lo] + nums[hi] > 0:
                    hi -= 1
                elif n + nums[lo] + nums[hi] < 0:
                    lo += 1
                else:
                    result.add((n, nums[lo], nums[hi]))
                    hi -= 1
                    lo += 1
        return [list(t) for t in result]