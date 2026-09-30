class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first: remore blank spaces then with 2 pointer low and high, check if they are equal until l <= h
        newS = [c.lower() for c in s if c.isalnum()]
        l, h = 0, len(newS) - 1
        while l <= h:
            if newS[l] != newS[h]:
                return False
            l += 1
            h -= 1
        return True