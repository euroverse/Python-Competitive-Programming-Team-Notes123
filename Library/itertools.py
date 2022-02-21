from itertools import combinations, permutations, product

''' [ Itertools Library : Product ]
- 중복 순열 = cartesian product = 데카르트 곱 = (n-r)!
: 둘 이상 iterable의 모든 조합을 구할 수 있다.
  = 여러개의 리스트(튜플)을 product함수에 넣어주면
    각 리스트(튜플)마다 하나씩 뽑은 순열을 반환해준다.
'''

list_ = [(1, 3), ('a', 'b'), ('!', '@')]
pd1 = list(product(*list_))
# [(1, 'a', '!'), (1, 'a', '@'), (1, 'b', '!'), (1, 'b', '@'),
# (3, 'a', '!'), (3, 'a', '@'), (3, 'b', '!'), (3, 'b', '@')]

# repeat의 역할은 product에 넣은 리스트(튜플)을 배로 늘려줌
pd2 = list(product(*list_, repeat = 2))
# [(1, 'a', '!', 1, 'a', '!'), (1, 'a', '!', 1, 'a', '@')...

# repeat을 이용해서 중복 순열 구하기 가능
list_2 = [1, 2, 3]
pd3 = list(product(list_2, repeat = 2))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
