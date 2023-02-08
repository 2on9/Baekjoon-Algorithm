# 동전의 종류 중 가장 큰 것부터 나누면 동전의 개수를 최소화시킬 수 있다.
N, K = map(int, input().split())

coin = []
cnt = 0
for _ in range(N):
    coin.append(int(input()))
for i in range(N-1, -1, -1):
    if coin[i] <= K :
        cnt += K // coin[i]
        K = K % coin[i]
        if K == 0:
            break

print(cnt)