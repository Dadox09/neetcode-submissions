class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() ;
        result = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            l = k+1 ; r = len(nums) - 1
            while l < r:
                summ = nums[l] + nums[r] + nums[k]
                if summ == 0:
                    result.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif summ < 0: l += 1
                else: r -= 1
        return result