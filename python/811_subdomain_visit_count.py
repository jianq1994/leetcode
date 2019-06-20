class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)
            labels = domain.split('.')
            subdomains = []
            for i in range(len(labels)):
                subdomains.append('.'.join(labels[i:]))
            for subdomain in subdomains:
                if subdomain in dic:
                    dic[subdomain] += count
                else:
                    dic[subdomain] = count
        ans = []
        for item in dic:
            ans.append(str(dic[item])+' '+item)
        return ans