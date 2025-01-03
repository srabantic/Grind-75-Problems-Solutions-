"""
Trie Tree:
It is a tree like data structure with the following properties
- Each node represents a character of a string 
- Each character is connected by an edge 
- The root node represents an empty strig//char
- Each path from the root to a leaf (or marked node) represents a stored string

Structure of a trie tree:

Root Node: The starting point of the trie, which is empty.
Child Nodes: Each child node represents the next character in a string.
End of Word Marker: A special marker (e.g., a boolean flag) is used to indicate the end of a valid word.

Characteristics of a Trie tree:

Hierarchical Storage: Strings with the same prefix share a common path in the trie.
Edge Labeled with Characters: Each edge connects nodes with specific characters.
Efficient Prefix Matching: Searching for strings with a common prefix is very fast because the shared prefixes are stored together.
Space Optimization: Though it can use a lot of memory for long strings with little overlap, it saves space for a dataset with many overlapping prefixes.


Leetcode Problem
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
            
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("app"))
print(obj.startsWith("ap"))
print(obj.startsWith("al"))