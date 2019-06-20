from copy import deepcopy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        if not graph:
            return []
        visited = []
        cur = 0
        tar = len(graph)-1
        
        def dps(graph,visited,cur,tar):
            res = []
            for i in graph[cur]:
                if i == tar:
                    res.append([cur,tar])
                elif i not in visited:
                    subvisited = deepcopy(visited)
                    subvisited.append(cur)
                    subres = dps(graph, subvisited, i, tar)
                    for sub in subres:
                        tmp = [cur]
                        tmp.extend(sub)
                        res.append(tmp)
            return res
        
        return dps(graph, visited, cur, tar)
            