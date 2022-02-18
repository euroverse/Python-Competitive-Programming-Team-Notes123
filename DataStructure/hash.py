''' [ Hash ]
- 파이썬에서는 Dictionary 자료구조를 통해 해시를 제공한다
- 리스트와 달리 인덱스가 아닌 Key를 통해 Value를 얻는다. (=Not Sequential)
- Map과 Set등에 이용 가능.
'''

# 생성
# 1번처럼 dict로 딕셔너리를 만들 때 Key는 자동으로 문자열로 바뀜.
dic1 = dict(euro=1, egoing=2, elon=3)
dic2 = dict([('euro', 1), ('egoing', 2), ('elon', 3)])
dic3 = {'euro': 1, 'egoing': 2, 'elon': 3}

# Value 가져오기
value1 = dic1['euro']
value2 = dic2.get('euro', 0) # 해당하는 value가 없으면 0을 대신 반환

# 삭제
del dic1['egoing']    # 해당 키가 없다면 keyError
dic2.pop('egoing', 0) # 해당 키가 없다면 0을 대신 반환

# 순회
# dic.keys(): only key, dic.values(): only value, dict.items(): either
for key in dic3:
    print(key, dic3[key], end=" ")

for key, value in dic3.items():
    print(key, value, end=" ")