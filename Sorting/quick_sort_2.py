n = 5
data = [8, 5, 4, 7, 2]

''' Quick sort 2
: 파이썬의 장점 (리스트 슬라이싱과 컴프리헨션)을 이용한 구현
'''

def quick_sort2(data):
    # 리스트가 비거나, 원소가 하나인 경우 종료
    if len(data) <= 1:
        return data
    
    pivot = data[0]    # 피벗은 첫번째 원소
    tail = data[1:]   # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [y for y in tail if pivot < y]
    
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

sorted_data = quick_sort2(data)
print(sorted_data)