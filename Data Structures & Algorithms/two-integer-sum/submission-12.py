class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the fact that only 1 pair of i and j satisfies the task means that nums has got no duplicates. 
        #so use enumerate to asses the indexes -> store in a dictionarie the nums already seen and, for every iteration check
        seen = {}

        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n] , i]
            
            seen[n] = i
        return []
