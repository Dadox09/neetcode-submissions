class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first: remore blank spaces then with 2 pointer low and high, check if they are equal until l <= h
        newS = [c.lower() for c in s if c.isalnum()]
        lo, hi = 0, len(newS) - 1

        while lo < hi:
            if newS[lo] == newS[hi]:
                lo += 1
                hi -= 1
            else:
                return False
        return True