class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in nums:
            x[i] = 1 + x.get(i,0)
        x2 = defaultdict(list)
        for key, value in x.items():
            x2[value].append(key)
        print(x2)
        v = list(x2.keys())
        print(v)
        l = []
        for i in range(k):
            z = v.index(max(v))
            l += x2[v[z]]
            v.pop(z)
            if v==[]:
                break
            if len(l)>=k:
                l = l[:k]
                break
        return l
