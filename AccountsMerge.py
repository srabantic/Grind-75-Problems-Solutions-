from typing import List, DefaultDict
"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Notes:
    We use the Union Find data structure to solve this problem. 
    1. Instantiate an instance of union find 
    2. Create a dictionary which will map email -> account index 
        This loop is responsible for merging all accounts that shares an email.
    3. Create a default dict which values will be list of items mapping -> index of account -> [emails]
        This loop is responsible for grouping all email address that belong to the same account 
    Note that step 2 and 3 serves diff purpose. 
    For example: 
        After step 2, we might have a dict such as 
                {'JohnSmith@gmail.com' : 1, 
                'JognNewYowrk@gmail.com' : 1
                'JohnBolbe@gmail.com' : 2}
        If in the original accoutn list, we had another JohnSmith@gmail.com, the union find in this 
        step will merge the accounts 1 and 2 together but this dict does not give us a list of 
        all emails which belongs to account 1. 
        Hence, we need step 3, which should give us 
        {1 : [JohnSmith@gmail.com', 'JognNewYowrk@gmail.com', 'JohnBolbe@gmail.com]}]
    4. Loop through all elements of the emailGroup dict to format the output. 

    Time Complexity: 
        O(E log E), where E = total number of emails for all acounts
        Another way to represent -> O((n * m) log (n * m)), where n*m = E 
    Space Complexity: 
        O(E), where E = total number of emails for all acounts
        Another way to represent -> O(n * m) where n*m = E 

"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # We need to define an instance of union find
        uf = UnionFind(len(accounts))
        # define a dictoinary => email -> account index 
        emailToAccount = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAccount:
                    uf.union(i, emailToAccount[e])
                else:
                    emailToAccount[e] = i
        

        # This dictionary will map index of account -> list of emails 
        emailGroup = DefaultDict(list)
        for e, i in emailToAccount.items():
            parent = uf.find(i)
            emailGroup[parent].append(e)
        
        res = []
        for i in emailGroup.keys():
            name = accounts[i][0]
            res.append([name] + [sorted(emailGroup[i])])
        return res


class UnionFind:
    def __init__(self, n):
        # define a hasmap for parent 
        self.par = {}
        # define a hashmap for rank(height)
        self.rank = {}
    
        for i in range(0, n+1): # n = number of nodes 
            self.par[i] = i # set each nodes parent to be itself 
            self.rank[i] = 0 # we set the height of each node to be 0 at the begining 
    
    # Find the parent of n using path compression 
    def find(self, n):
        p = self.par[n]
        ## recall that when a node is a parent of itself, that's when we know 
        # we have reached the root node
        # That's why in this while loop, we check whethe the parent node is a child of itself 
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] # make the current node's parent to point to it's granfparent
            p = self.par[p]
        return p
    
    # Decide if union between two node is possible 
    def union(self, n1, n2):
        # Find the parent of each node 
        p1 = self.find(n1)
        p2 = self.find(n2)
        # If they are pointing to the same parent, that means 
        # a union is not possible and they have a cycle.
        if p1 == p2:
            return False  
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
solutoion = Solution()
print(solutoion.accountsMerge(accounts))
