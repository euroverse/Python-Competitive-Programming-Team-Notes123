''' [ Binary Search (Iterative Method) ]
- 이진 탐색은 "정렬된" 리스트에서 범위를 좁혀가며 탐색한다.
- O(logN) 시간복잡도를 가지며, 특히 탐색범위가 매우 클 때 사용하면 유용하다.

- 재귀 함수 또는 반복문으로 구현할 수 있다.
- 이진 탐색 관련 파이썬 라이브러리 "python_binary_search_library.py" 참고
'''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # If the target is found, return the mid index.
        if array[mid] == target:
            return mid
        # If the value of the mid index is greater than the target, search the left part.
        elif array[mid] > target:
            end = mid - 1
        # If the value of the mid index is smaller than the target, search the right part.
        else:
            start = mid + 1
    return None

n = 10
target = 13
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = binary_search(array, target, 0, n - 1)
if result == None:
    print(None)
else:
    print(result + 1)
    
''' 아래는 반복문을 이용한 일반적인 형태의 이진탐색 '''
answer = 0
start, end = 0, 10**9
while start <= end:
    mid = (start+end)//2
    
    # 조건문이 True인 경우
    if condition():
        answer = mid    # 조건문에 부합하는 값은 미리 저장해둠.
        start = mid +1
    
    # 조건문이 False인 경우
    else:
        end = mid -1

print(answer)
