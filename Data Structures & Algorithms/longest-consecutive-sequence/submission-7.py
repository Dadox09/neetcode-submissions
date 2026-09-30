class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for n in numSet: #O(n)
            if n-1 not in numSet: #O(1)
                length = 1
                while n+length in numSet: #max O(n)
                    length += 1
                longest = max(length, longest)
        return longest