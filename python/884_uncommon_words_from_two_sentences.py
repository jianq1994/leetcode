from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        S = (A+' '+B).split(' ')
        ans = []
        count = Counter(S)
        for word in count:
            if count[word] == 1:
                ans.append(word)
        return ans