n = 5
data = [8, 5, 4, 7, 2]

''' Insertion Sort
: 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 "삽입"한다.
=> 데이터가 거의 정렬되어 있을 때 빠르게 동작, O(N) 기대.
'''
for i in range(1, n):    # 처리되지 않은 데이터를 하나씩 골라
    for j in range(i, 0, -1): # The variable j decreases from i to 1.
        if data[j - 1] > data[j]: # Move forward.
            data[j - 1], data[j] = data[j], data[j - 1] # Swap.
        else: # When reaching a smaller value, then stop.
            break

for x in data:
    print(x)
