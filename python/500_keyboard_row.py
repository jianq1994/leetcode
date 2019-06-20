Row = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if not words:
            return []
        ans = []
        for word in words:
            flag = 0
            for i in range(3):
                if word[0] in Row[i]:
                    for c in word:
                        if c not in Row[i]:
                            flag = 1
                            break
            if not flag:
                ans.append(word)
        return ans
        