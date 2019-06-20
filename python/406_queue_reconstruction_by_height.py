class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:-x[0]*1100+x[1])
        ans = []
        for person in people:
            ans.insert(person[1],person)
        return ans
        