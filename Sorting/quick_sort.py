n = 5
data = [8, 5, 4, 7, 2]

''' [ Quick Sort ]
- 분할 정복(Divide & Conquer)의 일종 (이외에 MergeSort와 하노이의탑 등이 있다.)
- 이상적인 경우 분할이 절반씩 일어나므로 O(NlogN)을 기대할 수 있으며, 최악의 경우 O(N^2)이다.

- 오름차순 정렬할 때 분할 과정
1. 기준 데이터(피벗)를 설정한다. (보통의 경우 가장 첫번째 원소)
2. 리스트의 두번째 원소에서부터 가장 처음 나온 '피벗보다 큰 원소'를 선택한다.
3. 리스트의 마지막 원소에서부터 가장 처음 나온 '피벗보다 작은 원소'를 선택한다.
4. 위에서 선택한 두 원소의 위치를 서로 바꾼다.
5. ②~④ 과정을 반복하다가 선택한 두 원소의 위치가 엇갈리는 경우,
   피벗과 '피벗보다 작은 원소'의 위치를 서로 바꾼다.   
* 이후 왼쪽 묶음과 오른쪽 묶음에 대해 각각 분할 과정을 재귀적으로 수행한다.
'''

def quick_sort1(start, end):
    if start >= end: # If the subarray size is 1, exit the function.
        return
    pivot = start # The pivot is the first element of the subarray.
    left = start + 1
    right = end
    while left <= right:
        # Until finding an element bigger than the pivot,
        while left <= end and data[left] <= data[pivot]:
            left += 1
        # Until finding an element smaller than the pivot,
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right: # If two elements miss each other,
            data[right], data[pivot] = data[pivot], data[right]
        else: # If two elements don't miss each other,
            data[left], data[right] = data[right], data[left]
    # Sort the left part and right part respectively.
    quick_sort(start, right - 1)
    quick_sort(right + 1, end)

quick_sort(0, n - 1)

for x in data:
    print(x)
