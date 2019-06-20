class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        s1,t1 = a.split('+')
        x1,y1 = int(s1),int(t1[:-1])
        s2,t2 = b.split('+')
        x2,y2 = int(s2),int(t2[:-1])
        x3 = x1*x2 - y1*y2
        y3 = x1*y2 + x2*y1
        return str(x3)+'+'+str(y3)+'i'
        class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        s1,t1 = a.split('+')
        x1,y1 = int(s1),int(t1[:-1])
        s2,t2 = b.split('+')
        x2,y2 = int(s2),int(t2[:-1])
        x3 = x1*x2 - y1*y2
        y3 = x1*y2 + x2*y1
        return str(x3)+'+'+str(y3)+'i'
        