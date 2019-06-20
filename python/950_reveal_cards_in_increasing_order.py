class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        pop = []
        dic = {}
        for i in range(len(deck)):
            dic[i] = i
        value = len(deck)
        while(1):
            pop.append(min(dic, key=dic.get))
            dic.pop(pop[-1])
            if not dic:
                break
            n = min(dic, key=dic.get)
            dic[n] = value
            value += 1
        deck.sort()
        ans = [0] * len(deck)
        for num,i in enumerate(pop):
            ans[i] = deck[num]
        return ans

##用优先队列应该能提升performance