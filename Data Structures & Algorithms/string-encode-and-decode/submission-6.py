class Solution:

    def encode(self, strs: List[str]) -> str:
        # s = str(len(strs))+"_"
        s = ""
        for i in strs:
            s = s+str(len(i))+"_"+i
        return s

    def decode(self, s: str) -> List[str]:
        li =[]
        # print(s)
        # x = 1
        # for i in range(len(s)):
        #     if s[i]=="_":
        #         l=int(s[:i])
        #         s=s[i+1::]
        # print(l)
        print(s)
        j=0
        i=0
        while i < len(s):
            print(i)
            if s[i]=="_":
                l=int(s[j:i])
                print(l)
                li.append(s[i+1:i+l+1:])
                i = i+l+1
                j=i
            else:
                i += 1
        return li
        
