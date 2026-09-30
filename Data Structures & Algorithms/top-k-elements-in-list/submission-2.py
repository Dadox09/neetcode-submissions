class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency -> bucket algorithm
        #1 - count the frequence and then build the buckets
        #2 - build the buckets 
        #3 count backwards the buckets 

        count = collections.defaultdict(int) #key = n, value = frequency
        freq = [[] for i in range(len(nums) + 1)] #index = frequency, value = list of numbers
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        

