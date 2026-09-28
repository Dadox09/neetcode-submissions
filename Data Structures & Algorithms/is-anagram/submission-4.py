class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #idea is to order in an alphabetic order the strings and checking equality. 
        #return sort(s) == sort(t)
        return sorted(s) == sorted(t)