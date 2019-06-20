class Solution:
    def reorderLogFiles(self, logs):
        def k(log):
            head, val = log.split(" ",1)
            return (1,) if val[0].isdigit() else (0, val, head)
        
        return sorted(logs,key=k)

        