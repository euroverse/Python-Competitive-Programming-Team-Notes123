''' [ Combination_with_Repetition ]
- 중복 조합 : 중복을 허용하여 서로다른 n개중 r개를 선택하는 경우의 수

- 경우의 수를 구하는 문제일 때, 중복 조합을 이용해 풀 수 있는 경우가 간혹 있다. (ex. BOJ2225)

- 칸막이와 구슬을 떠올리자.    ex. OIOOIOOO = 서로다른 3개중 6개를 선택하는 방법 中 1
- n 종류 -> 칸막이가 n-1개
- r 개를 선택 -> 구슬이 r개
    => nHr = (n+r-1)Cr = fac(n-1+r) // {fac(n-1)*fac(r)}

[유튜브 강의] https://youtu.be/M-HJOboEc_M
'''