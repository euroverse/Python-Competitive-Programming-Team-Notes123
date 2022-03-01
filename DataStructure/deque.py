from collections import deque

''' deque는 양방향 삽입 삭제가 가능하며, 이를 활용해 큐 대신에 사용한다.

deque는 양쪽 끝을 당기고 밀도록 최적화되어 있어서
심지어 전용 rotate() method가 존재한다.
BOJ.2346 풍선 터뜨리기 문제 등에 적합하다.
'''


items = deque([1, 2])
items.append(3)        # deque == [1, 2, 3]
items.rotate(1)        # The deque is now: [3, 1, 2]
items.rotate(-1)       # Returns deque to original state: [1, 2, 3]
item = items.popleft() # deque == [2, 3]