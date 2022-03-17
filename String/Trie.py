''' [ Trie ]
- 트라이 : 문자열을 저장 & 탐색하기 위해 사용되는 Search Tree의 일종.
- 입력된 단어를 저장|탐색하는 시간복잡도는 O(m)이다. 이때, m은 입력된 단어의 길이이다.

★ 시간복잡도가 좋지만, 해시(dict)만큼 빠르지는 않다.
   문제 상황에 적절하게 사용하자.

- 다음 글자를 가리키는 방법에 따라 구현 방법이 다르다.
    1. 해시(dict)를 이용한 방법 (아래 코드)
    2. 리스트(array)를 이용한 방법 (A~Z를 1부터 26까지로 매칭)

[깃허브 강의] https://youseop.github.io/2020-11-09-BAEKJOON-14425_%EB%AC%B8%EC%9E%90%EC%97%B4%EC%A7%91%ED%95%A9/
[유튜브 강의] https://youtu.be/WooOuXIiRjE
[파이썬 어노테이션] https://wiserloner.tistory.com/486
'''

class TrieNode:
    def __init__(self, data = None):
        self.data = data
        self.isEnd = False
        self.links = {}
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # 입력된 단어 word를 트라이에 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            
            # ch에 해당하는 링크가 없으면 만들어줌
            if ch not in node.links:
                node.links[ch] = TrieNode(ch)
            
            # ch에 해당하는 링크로 이동
            node = node.links[ch]
        node.isEnd = True
    
    # 입력된 단어 word가 존재하는지 검색
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.links:
                return False
            node = node.links[ch]
        return node.isEnd
    
    # 접두사 str로 시작하는 단어가 있는지 찾기
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.links:
                return False
            node = node.links[ch]
        return True
        
        
trie = Trie()

trie.insert("baby")
trie.insert("ball")

print(trie.search("baby"))    # True
print(trie.search("ball"))    # True
print(trie.search("bake"))    # False
        
        
        
        