class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf=0
        res=0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            maxf = max(freq[s[r]],maxf)
            while r-l+1-maxf > k:
                freq[s[l]] -= 1
                l+=1
            
            if r-l+1-maxf <= k:
                res = max(r-l+1,res)
            # print(l,r,maxf)
        return res

        

            


        