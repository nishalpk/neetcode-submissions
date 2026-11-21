class Solution:
    def isValid(self, s: str) -> bool:
        m  = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        l = deque()


        for i in s:
            if i in "{([":
                l.append(i)
            if i in "}])":
                if l and l[-1]==m[i]:
                    l.pop()
                else:
                    return False
                
        
        return len(l)==0
        