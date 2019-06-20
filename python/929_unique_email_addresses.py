class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailset = set()
        for email in emails:
            local, domain = email.split("@")
            clocal = local.split('+')[0].replace('.','')
            emailset.add(clocal + '@' + domain)
        return len(emailset)
