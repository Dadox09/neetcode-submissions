class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            seen = {}
            for i, n in enumerate(nums):
                diff = target - n
                if diff in seen:
                    return [seen[diff], i]
                seen[n] = i