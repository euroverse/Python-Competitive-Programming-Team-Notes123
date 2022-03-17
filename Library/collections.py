from collections import deque
from collections import Counter

''' [ collections Library : deque ]
- 덱 자료형을 쉽게 구현할 수 있게한다. (=> 큐 자료형 생성에 많이 이용됨.)
- 덱은 리스트의 앞 뒤 모두에서 삽입 삭제가 가능하며, O(1) 시간복잡도를 갖는다.
'''
q = deque([1, 2, 3])
q.append(4)
k = q.popleft()


''' [collections Library : Counter ]
- 반복 가능한 (Iterable) 객체가 주어졌을 대 내부의 원소가 몇 번씩 등장했는지 세어줌.
'''
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])    # 3
print(counter['green'])   # 1
print(dict(counter))      # {'red': 2, 'blue': 3, 'green': 1}

# 자주 등장하는 원소 상위 N개 출력하기
N = 2
print(counter.most_common(N)) # [('blue', 3), ('red', 2)]