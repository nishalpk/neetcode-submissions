class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for s in strs:
            k = [0]*26
            for l in s:
                k[ord(l)-ord('a')] += 1
            x[tuple(k)].append(s)


        return list(x.values())