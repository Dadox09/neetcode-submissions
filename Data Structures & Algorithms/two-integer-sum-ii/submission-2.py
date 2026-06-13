class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for n in numbers:
            if target - n in numbers and n < target - n:
                result = [numbers.index(n) + 1, numbers.index(target-n) + 1]
        return result
        