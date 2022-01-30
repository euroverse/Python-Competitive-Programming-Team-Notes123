n = 5
data = [8, 5, 4, 7, 2]

''' Selection Sort
: 처리되지 않은 데이터 중에서 가장 작은 데이터를 "선택"하여 맨 앞에 있는 데이터와 바꾸는 것을 반복함.
'''
for i in range(n):
    min_index = i # The index of the minimum value.
    for j in range(i + 1, n):    # 위치가 결정되지 않은 데이터 중에서
        if data[min_index] > data[j]:    # 가장 작은 데이터의 인덱스를 기억
            min_index = j
    data[i], data[min_index] = data[min_index], data[i] # Swap.

for x in data:
    print(x)

