class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #longest substring -> slinding window

        seen = set()
        l = 0
        longest = 1

        if not s:
            return 0

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest