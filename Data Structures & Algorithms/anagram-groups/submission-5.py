from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #check anagram and add them in a hashmap (dict)

        if not strs:
            return [""]

        result = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            result[sortedS].append(s)
        return list(result.values())