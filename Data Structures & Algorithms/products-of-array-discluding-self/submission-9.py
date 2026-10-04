class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #array output at every position should have the product of the entire array nums except himself
        #i could solve without the division using prefix_prod e suffix_prod, so product left and right
        #then for every output[i] = prefix[i] * suffix[i]

        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 1
        suffix[n - 1] = 1

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for y in range(n - 2, -1, -1):
            suffix[y] = nums[y + 1] * suffix[y + 1]

        result = [0] * n

        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result