from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #per ogni word in strs se reversed(word) in seen allora la inserisco li, altrimenti la inserisco e basta.
        #seen deve essere hash table -> seen = {}
        #controllo quindi if seen[reversed(word)] : seen[reversed(word)].append(word)

        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        