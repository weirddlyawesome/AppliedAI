
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


        

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            i = ord(char) - ord('a')

            if not cur.children[i]:
                cur.children[i] = TrieNode()

            cur = cur.children[i]

        cur.eow = True
        

    def search(self, word: str) -> bool:
        
        def dfs(i, curr):

            if not curr:
                return False
            if i >= len(word):
                return curr.eow

        
            if word[i] != '.':
                index = ord(word[i]) - ord('a')
                if curr.children[index]:
                    return dfs(i +1, curr.children[index])
            else:
                for ptr in curr.children:
                    if dfs(i+1, ptr):
                        return True

            return False
        
        return dfs(0, self.root)
        
