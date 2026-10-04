class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        max_count = 1

        if not nums:
            return 0

        for n in nums:
            if n - 1 not in nums:
                #n is a first of a possible consecutive sequence
                count = 1
                while n + count in nums:
                    count += 1
                max_count = max(max_count, count)
        return max_count
