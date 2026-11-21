class Solution:

    def encode(self, strs: List[str]) -> str:
        # s = str(len(strs))+"_"
        l = []
        s = ""
        for i in strs:
            l.append(str(len(i)))
            l.append('_')
            l.append(i)
            # +"_"+i
        s = "".join(l)
        return s

    def decode(self, s: str) -> List[str]:
        li =[]
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
        
