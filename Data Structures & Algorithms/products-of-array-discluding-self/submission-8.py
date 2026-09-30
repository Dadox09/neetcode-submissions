class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #except nums[i] means prefix and suffix(left and right), then prefix * suffix
        #so initialize prefix and suffix, lenght n = len(nums), prefix[0] = 1, suffix[n - 1] = 1
        #then calculate prefix and suffix in for loops

        n = len(nums)
        prefix = [0] * n 
        suffix = [0] * n
        res = [0] * n

        prefix[0] = 1
        suffix[n - 1] = 1 
        
        #build prefix
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        #build suffix
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        #build the result
        for i in range(0, n):
            res[i] = prefix[i] * suffix[i]

        return res    