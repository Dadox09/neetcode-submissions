class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #longest substring -> contiguous -> sliding window
        #count c in s: if some c already in seen[]: while in seen, delete and count -= 1

        if not s:
            return 0

        seen = set() 
        lo = 0
        max_count, count = 1, 0

        for hi in range(len(s)):
            if s[hi] in seen:
                while s[hi] in seen:
                    seen.remove(s[lo])
                    lo += 1
                    count -= 1
            seen.add(s[hi])
            count += 1
            max_count = max(max_count, count)
        return max_count
