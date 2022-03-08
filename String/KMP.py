''' [ KMP (Knuth-Morris-Pratt) ]
: 두 문자열 S1과 S2가 주어졌을 때, S2가 S1의 서브스트링인지 탐색하는 알고리즘이다.

- S1과 S2의 길이가 각각 N, M일 때,
  일반적인 방법(S1의 모든 서브스트링을 S2와 비교)으로 탐색을 하면 O(N*M)이다.
  KMP 알고리즘을 사용할 경우 O(N)까지 최적화 할 수 있다는 것이 중요하다.
  
  "하지만, KMP는 다소 복잡하므로 코테에서는 Rabin-Karp를 이용하길 바람"

- Reference : https://youtu.be/UcjK_k5PLHI
- 대표적인 문제 : BOJ-16916.부분문자열
'''