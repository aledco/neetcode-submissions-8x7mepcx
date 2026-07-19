class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        
        def sameAccount(a1, a2):
            i = j = 0
            while i < len(a1) and j < len(a2):
                if a1[i] == a2[j]:
                    return True
                
                if a1[i] < a2[j]:
                    i += 1
                else:
                    j += 1
            return False
        
        def dedup(account):
            offset = 0
            for i in range(1, len(account)):
                if account[i] == account[i-1]:
                    offset += 1
                else:
                    account[i-offset] = account[i]
                i
            return account[:len(account)-offset]

        def merge(a1, a2): 
            merged = []
            i = j = 0
            while i < len(a1) and j < len(a2):
                if a1[i] == a2[j]:
                    merged.append(a1[i])
                    while i < len(a1) and a1[i] == merged[-1]:
                        i += 1
                    while j < len(a2) and a2[j] == merged[-1]:
                        j += 1
                elif a1[i] < a2[j]:
                    merged.append(a1[i])
                    i += 1
                else:
                    merged.append(a2[j])
                    j += 1

            return merged + a1[i:] + a2[j:]

        def mergeAll(accounts):
            if len(accounts) <= 1:
                return accounts
            
            merged = []
            while len(accounts) > 0:
                curr = accounts.pop()
                unmerged = []
                anymerged = False
                while len(accounts) > 0:
                    account = accounts.pop()
                    if sameAccount(curr, account):
                        curr = merge(curr, account)
                        anymerged = True
                    else:
                        unmerged.append(account)
                
                accounts = unmerged
                if anymerged:
                    accounts.append(curr)
                else:
                    merged.append(curr)
            return merged

        names = defaultdict(list)
        for account in accounts:
            names[account[0]].append(
                dedup(
                    list(sorted(account[1:]))
                )
            )
        
        res = []
        for name in names.keys():
            for emails in mergeAll(names[name]):
                res.append([name] + emails)
        return res
        
        
