class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def ok(k: int) -> bool:
            count = 0
            for p in piles:
                count += (p + k - 1) // k
            return count <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            if ok(k):
                hi = k 
            else:
                lo = k + 1
        return lo