# 끝나는 시간이 빨라야 다음 회의를 진행시킬 수 있다. 끝나는 시간이 빠른 회의 순으로 진행을 시켜주면 된다.
N = int(input())
meeting = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1],x[0])) #끝나는 시간으로 먼저 정렬하되 (1, 2) (2, 2)와 같은 예가 있으므로 끝나는 시간이 같을 경우, 시작하는 시간이 빠른 순으로 정렬해준다.
ans = end = 0
for s, e in meeting:
    if s >= end:
        ans += 1
        end = e
print(ans)