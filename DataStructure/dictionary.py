from collections import defaultdict
# zip을 이용하면 주어진 데이터를 이용해 쉽게 dictionary를 만들 수 있다.
fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]

dic_ = dict(zip(fruit, price)) 
# {'apple' : 3200, 'grape' : 15200, 'orange' : 9000, 'banana' : 5000}


''' 일반적으로, 딕셔너리에서 없는 값을 찾으려고 하면 오류가나므로
in 연산자를 이용해 데이터가 있는지 확인하고, 없으면 값을 추가하고 있으면 출력하는 방식을 사용한다.
그러나, setdefault를 사용하면 그럴필요가없다.
setdefault는 딕셔너리에 값이 있을 때는 해당 값을 리턴하고
없으면 넘겨준 값을 추가하고 추가한 값을 리턴한다.

get과 다른 점은 "없으면 원소를 추가"한다는 것이다.
'''
print(dic_.setdefault('strawberry', -1))
print(dic_)
print(dic_.get('strawberry', -2))

print(sorted(dic_.items())) # sorted는 "컨테이너형 데이터를 받아 정렬된 리스트를 돌려주는 함수"이다.


''' setdefault 메소드를 활용한
유사 딕셔너리가 있다. 이것을 defaultdict라고 부른다.
from collections import defaultdict
딕셔너리에 값이 없으면 인자로 념겨준 값을 default값으로 만듦.
setdefault를 암묵적으로 실행해준다고 볼 수 있음.
'''
movie_review = [('Train to Busan', 4), ('Clementine', 5), ('Parasite', 4.5), ('Train to Busan', 4.2), ('Train to Busan', 4.5), ('Clementine', 5)]

index = defaultdict(list)

for review in movie_review:
    index[review[0]].append(review[1]) # {'Train to Busan': [4, 4.2, 4.5], 'Clementine': [5, 5], 'Parasite': [4.5]}
