class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def k(word):
            ans = []
            for i in word:
                ans.append(order.index(i))
            return tuple(ans)
        
        return sorted(words,key=k) == words