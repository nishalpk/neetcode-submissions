class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in nums:
            x[i] = 1 + x.get(i,0)
        f = [[] for i in range(len(nums)+1)]
        h = 0
        for key, value in x.items():
            if value>h:
                h=value
            f[value].append(key)
        l =[]
        for i in range(h,0,-1):
            l = l + f[i]
            if len(l)>k:
                l = l[:k]
                break
        return l

