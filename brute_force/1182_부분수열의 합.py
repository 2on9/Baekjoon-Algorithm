# N의 최대는 20, 최대의 경우의 수는 2^20 = 1048576 이므로 모든 조합(경우의 수)를 따져서 합을 구한 뒤, S와 같을 때 cnt를 추가해준다.
import itertools

N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1): # 1개를 선택하는 경우 ~ N개를 선택하는 경우의 수
    comb = itertools.combinations(num, i) 
    for x in comb:
        if sum(x) == S:
            cnt += 1

print(cnt)    