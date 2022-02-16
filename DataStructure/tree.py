''' [ Tree ]
- 트리(자유트리) : 사이클이 없는 연결 그래프
- 자유트리에서 하나의 정점을 루트로 정하면, "루트를 가진 트리"가 되며,
  이것을 간단히 '트리'라고 부른다. 이때 정점대신 노드란 용어를 사용한다.

- 이진 트리 : 자식 노드의 갯수(=최대 차수)가 2로 제한되는 트리
- 이진 탐색 트리 : 이진 트리 + (왼쪽자식<부모<오른쪽자식)조건

- 구조에 따라 AVL트리, 완전이진트리, 포화이진트리 등 다양하다.
- 외부 라이브러리 'anytree'를 통해 쉽게 구현이 가능하다.

참고 URL: 
https://geonlee.tistory.com/72 (이진탐색트리)
https://blog.naver.com/hunii123/222539583613
https://velog.io/@ash3767/python-Data-Structure
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        
class BinaryTree:
    def __init__(self, root):
        self.root = root