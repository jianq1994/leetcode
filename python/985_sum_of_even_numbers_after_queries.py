class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sumE = 0
        for a in A:
            if a%2 == 0:
                sumE += a
        for query in queries:
            if A[query[1]]%2 == 0 and query[0]%2 == 0:
                A[query[1]] += query[0]
                sumE += query[0]
                ans.append(sumE)
            elif A[query[1]]%2 == 0 and query[0]%2 != 0:
                sumE -= A[query[1]]
                A[query[1]] += query[0]
                ans.append(sumE)
            elif A[query[1]]%2 != 0 and query[0]%2 == 0:
                A[query[1]] += query[0]
                ans.append(sumE)
            else:
                A[query[1]] += query[0]
                sumE += A[query[1]]
                ans.append(sumE)
        return ans