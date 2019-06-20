Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans = set()
        for word in words:
            tran = ''
            for c in word:
                tran += Morse[ord(c)-ord('a')]
            trans.add(tran)
        return len(trans)