class Solution:
    def toLowerCase(self, str: str) -> str:
        BIG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        small = 'abcdefghijklmnopqrstuvwxyz'
        out = ''
        for num,s in enumerate(str):
            if s in BIG:
                out += small[BIG.index(s)]
            else:
                out += s
        return out