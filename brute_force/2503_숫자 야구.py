# 1~9까지의 서로 다른 숫자 3개 -> 9P3 = 504개 하나하나씩 비교하면 x3 완전탐색으로 구할 수 있다.
import itertools

N = int(input())
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(itertools.permutations(data, 3))

for _ in range(N):
    n, s, b = map(int, input().split())
    n = list(str(n))
    cnt = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= cnt # << (i=0일떄) 만약 0번째 원소가 답이 아니였으면, 그 0번째 원소는 없어졌을 것이다. 그리고 cnt = 1이 되었을텐데, (i=1일때) i는 i-cnt로 i는 0이 된다. 왜? 0번째 원소가 없어졌기 때문에 1번째 원소는 0번째 원소가 돼서 이렇게 해줘야 모든 숫자를 탐색할 수 있다.
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]: 
                ball += 1
        if (strike != s) or (ball != b):
            num.remove(num[i]) # 스트라이크, 볼 개수가 다르다면 없앤다.
            cnt += 1 # num에서 없앴으므로 cnt를 하나 추가해준다.
print(len(num))

        
