

def char_to_int(c):
    """ char 을 int 로 변환하는 함수 """
    return ord(c) - ord('a')


class TrieNode:

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = [None] * 26


# 소문자 알파벳만 처리가능
class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, key, data=None):
        node = self.root
        length = len(key)
        for level in range(length):
            index = char_to_int(key[level])

            # if current character is not present
            if not node.children[index]:
                node.children[index] = TrieNode(index, data)

            node = node.children[index]

    def search(self, key):
        node = self.root
        length = len(key)
        for level in range(length):
            index = char_to_int(key[level])
            if not node.children[index]:
                return None
            node = node.children[index]

        return node

