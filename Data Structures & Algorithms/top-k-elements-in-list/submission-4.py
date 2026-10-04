from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #return k most frequent -> bucket approach
        #bucket: key = frequency, value = number

        n = len(nums)
        bucket = [[] for i in range(n + 1)]
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
        for n, c in count.items():
            bucket[c].append(n)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i]:
                for n in bucket[i]:
                    result.append(n)
            if len(result) == k:
                return result

        