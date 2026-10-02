class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search -> l = 0, h = len(nums) - 1, within the loop, compute mid = (l + r) // 2
        #then update l or r in the correct way

        l , r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1