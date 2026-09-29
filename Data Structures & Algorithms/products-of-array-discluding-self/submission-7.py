class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left product x right product
        n = len(nums)
        
        leftP = [0] * n
        rightP = [0] * n
        res = [0] * n

        leftP[0] = 1
        rightP[n - 1] = 1

        for i in range(1, n):
            leftP[i] = nums[i - 1] * leftP[i - 1]

        for i in range(n - 2, -1, -1):
            rightP[i] = nums[i + 1] * rightP[i + 1]

        for i in range(n):
            res[i] = leftP[i] * rightP[i]

        return res

        