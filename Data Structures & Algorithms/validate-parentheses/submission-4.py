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
                if len(l)==0:
                    return False

                elif l[-1]!=m[i]:
                    return False
                l.pop()
        
        return len(l)==0
        