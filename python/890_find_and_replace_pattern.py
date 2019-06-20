class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        dic = {}
        idx = 0
        pa = ''
        for s in pattern:
            if s in dic:
                pa += dic[s]
            else:
                dic[s] = chr(ord('a')+idx)
                idx += 1
                pa += dic[s]
        ans = []
        for word in words:
            wdic = {}
            idx = 0
            wpa = ''
            flag = 0
            for num,s in enumerate(word):
                if s in wdic:
                    if wdic[s] != pa[num]:
                        flag = 1
                        break
                    wpa += wdic[s]
                else:
                    wdic[s] = chr(ord('a')+idx)
                    idx += 1
                    if wdic[s] != pa[num]:
                        flag = 1
                        break
                    wpa += wdic[s]
            if not flag:
                ans.append(word)
            
                    
        return ans
        