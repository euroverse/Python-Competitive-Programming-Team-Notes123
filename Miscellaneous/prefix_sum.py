n = 5
data = [10, 20, 30, 40, 50]

''' [ Make prefix sum array ]
- 접두사 합 : 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
'''
summary = 0
prefix_sum = [0]
for i in data:
    summary += i
    prefix_sum.append(summary)

    
''' [ Get interval sum ]
- 구간 합 : 특정 구간의 모든 수의 합
'''
left = 2
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])
