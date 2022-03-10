import math

''' [ Check if a number is prime ]
- 소수 판별
- 기본적인 구현 : 반복문으로 1부터 쭉 검사
- 개선된 구현 : 약수의 성질을 이용, 가운데 약수(제곱근)까지만 검사

'''
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True


''' [Sieve of Eratosthenes]
- 에라토스테네스의 체 : 2부터 N까지 범위에 존재하는 모든 소수 찾기
★ O(NloglogN) 시간 복잡도를 가지며, 사실상 선형 시간에 가까울 정도로 빠름.
   단, 메모리가 많이 필요하다는 단점을 갖는다.

반 | 1. 아직 처리하지 않은 가장 작은 수 x를 찾는다.
복 | 2. x의 배수를 모두 제거한다. 단, x는 제거하지 않음.

★ 약수의 성질은 에라토스테네스의 체에도 적용듸므로, 제곱근까지만 검사해도 최종 결과와 같다.
ex. 1부터 26까지의 소수를 구할 때, (2, 3, 4, 5)의 배수만 제거해도 최종 결과와 같다.
'''
N = int(input())

# 처음엔 모든 수가 소수 (0과 1은 제외)
array = [False, False] + [True]*(N-1)    

for i in range(2, int(math.sqrt(N))+1):
    if array[i]:    # x가 소수인 경우 (= 처리되지 않은 수)
        for j in range(2*i, N+1, i): # 자기 자신을 제외한 배수는 모두 False
            array[j] = False
        

        
        
