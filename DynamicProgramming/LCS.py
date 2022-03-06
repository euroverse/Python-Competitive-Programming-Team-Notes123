''' [ LCS (Longes Common Subsequence) ]
- 최장 공통 부분 수열
: 두 수열(문자열)의 공통 부분 수열 중 가장 긴 것을 찾는 문제.

- DP 테이블을 이중리스트(행렬)로 구현한다.
- 두 부분 수열의 길이를 하나씩 늘려가며 모든 경우를 계산
  ex. 주어진 두 수열이 "ACAYKP", "CAPCAK"일 때..
  "A"와 "C"의 가장 긴 공통 부분 수열 -> 0
  "A"와 "CA"의 가장 긴 공통 부분 수열 -> 1
  ...
  "ACAYKP"와 "CAPCAK의 가장 긴 공통 부분 수열 -> 4

- 추가한 글자가 서로 같을 때 -> dp[y][x] = dp[y-1][x-1] + 1
  ex. 현재 두 부분 수열이 "ACA"와 "CAPCA"일 때..
  추가한 글자가 "A"로 일치하기 때문에,
  두 부분 수열이 "ACA"와 "CAPCA"일 때 최대 길이 = "AC"와 "CAPC"일 때 최대 길이 + 1

- 추가한 글자가 서로 다를 때 -> dp[y][x] = max(dp[y][x-1], dp[y-1][x])
  ex. 현재 두 부분 수열이 "ACAYKP"와 "CAPCAK"일 때..
  추가한 글자가 "P"와 "K"로 서로 다르기 때문에,
  두 부분 수열이 "ACAYKP"와 "CAPCAK"일 때 최대 길이
  = max( 두 부분 수열이 "ACAYK"와 "CAPCAK"일 때 최대 길이,
         두 부분 수열이 "ACAYKP"와 "CAPCA"일 때 최대 길이) 

Reperence : https://suri78.tistory.com/11
'''

S1 = input()
S2 = input()

# dp에 ZeroPadding을 추가하기 위해 (길이+1)
# -> 연산 시에 범위 밖으로 나가는 것을 예외처리 해주지 않아도 됨.
dp = [[0] * (len(S2)+1) for _ in range(len(S1)+1)]

for y in range(1, len(S1)+1):
    for x in range(1, len(S2)+1):
        
        # 최근에 추가한 글자가 서로 같을 때
        # ZeroPadding 추가한 것을 고려하여 인덱스-1을 비교
        if S1[y-1]==S2[x-1]:
            dp[y][x] = dp[y-1][x-1] + 1
        
        # 최근에 추가한 글자가 서로 다를 때
        else:
            dp[y][x] = max(dp[y][x-1], dp[y-1][x])

print(dp[-1][-1])
'''
[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 2, 2, 2]
[0, 1, 2, 2, 2, 3, 3]
[0, 1, 2, 2, 2, 3, 3]
[0, 1, 2, 2, 2, 3, 4]
[0, 1, 2, 3, 3, 3, 4]
'''