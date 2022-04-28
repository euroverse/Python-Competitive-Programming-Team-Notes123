''' [ Named Tuple ]
- 데이터를 담기위한 용도로 클래스를 사용하는 경우가 있다. (비효율적임)
    => Named Tuple로 각 원소에 이름을 부여해 동일한 기능 구현 가능 

- Named Tuple에서는 method 정의가 불가한 단점이 있음
    => Dataclass

- 관련 내용 : 
    Goorm Ai 자연어처리 전문가 양성 과정 9강.Advanced Data Structure
    https://zzsza.github.io/development/2020/07/05/python-namedtuple/
    https://www.daleseo.com/python-property/ (property, getter, setter 관련 내용)
'''
from collections import namedtuple

Score = namedtuple("Score", ['x', 'y', 'z'])

score = Score(10, 20, z=30)
print(score.x)        # Attribute명으로 참조
print(score[1])       # 인덱스로 참조
print(*score)         # Unpacking

# Error : 튜플이라서 값 변경 불가
# score[0] += 1

'''
- 아래 코드는 데이터만을 담기 위해 클래스 사용하는 예시
- property를 통해 Getter를 작성해야함.

class Score:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
'''
