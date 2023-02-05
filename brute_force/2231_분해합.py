# 1부터 N까지 모든 수를 체크하면 된다. 시간 복잡도는 O(N)이므로, N의 크기는 1,000,000까지이므로 2초라는 시간제한에 걸리지 않는다.

N = int(input())
for i in range(1, N):
    digits = [int(n) for n in str(i)]
    result = int(i) + sum(digits)
    if result == N:
        print(i)
        break