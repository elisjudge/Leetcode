class Solution:
    def __init__(self) -> None:
        pass
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            unique_emails.add((local, domain))
        return len(unique_emails)

    def numUniqueEmailsManual(self, emails: list[str]) -> int:
        unique_emails = set()
        
        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i+=1
            
            while e[i] is not "@":
                i+=1
            
            domain = e[i+1:]
            unique_emails.add((local, domain))
        
        return len(unique_emails)



emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

s = Solution()
print("Solution with inbuilt functions")
print(s.numUniqueEmails(emails1))
print(s.numUniqueEmails(emails2))
print()
print("Solution with Manual implementation")
print(s.numUniqueEmailsManual(emails1))
print(s.numUniqueEmailsManual(emails2))
print()