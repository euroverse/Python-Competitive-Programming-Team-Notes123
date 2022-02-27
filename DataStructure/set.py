''' [ Set ]
- 집합 자료구조
- 파이썬에서는 Set 자료형을 기본 제공한다.

교집합 set1 & set2    (set1.intersection(set2))
합집합 set1 | set2    (set1.union(set2))
차집합 set1 - set2    (set1.defference(set2))
대칭 차집합 set1 ^ set2
원소추가 set.update([1, 2, 3])
원소삭제 set.remove(1)

원소를 탐색하는 in 연산자의 시간 복잡도는 아래와 같다.
list, tuple : O(n)
set, dictionary : O(1) => 해시



Set의 원소를 정렬해서 출력하고 싶으면, sorted(list(set))할 필요 없이
sorted(set)을 하면 됨. sorted가 "컨테이너형 데이터를 받아 정렬된 리스트를 돌려주는 함수"이기 때문.
단, set.sort()는 해당되지 않음.
'''
set_ = set([1, 3, 5, 7, 6, 4, 2])
print(sorted(set_))