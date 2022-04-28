''' [ Dataclass ]
- 데이터를 담고, 간단한 method 정의 가능

- 관련 내용 : 
    Goorm Ai 자연어처리 전문가 양성 과정 9강.Advanced Data Structure
'''
from dataclasses import dataclass

@dataclass
class Coords3D:
    x: float
    y: float
    z: float = 0
        
    def norm(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

point = Coords3D(10, 20, 30)
print(point)
print(point.norm())