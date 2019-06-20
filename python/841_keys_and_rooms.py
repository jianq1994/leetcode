class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        closed = [1] * len(rooms)
        usablekey = [0]
        while(usablekey):
            num = usablekey.pop()
            if closed[num]:
                closed[num] = 0
                usablekey.extend(rooms[num])
        if not any(closed):
            return True
        return False