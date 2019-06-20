class Solution:
    def toGoatLatin(self, S: str) -> str:
        GLlist = S.split(" ")
        GL = ''
        for num, s in enumerate(GLlist):
            if s[0] in 'aeiouAEIOU':
                GL += s + 'ma' + 'a'*(num+1)
            else:
                GL += s[1:] + s[0] + 'ma' + 'a'*(num+1)
            GL += ' '
        
        return GL[:-1]