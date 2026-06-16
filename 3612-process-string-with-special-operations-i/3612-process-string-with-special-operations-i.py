class Solution:
    def processStr(self, s: str) -> str:
        t=[]
        for c in s:
            match c:
                case '*':
                    if t: t.pop()
                case '#':
                    t+=t
                case '%':
                    t=t[::-1]
                case _:
                    t+=c
        return "".join(t)