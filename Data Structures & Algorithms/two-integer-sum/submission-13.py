class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #while going through the list, save in dict seen numbers and with "if in" check in O(1) the difference
        seen = {}

        for i, n in enumerate(nums):
            
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i

        return []