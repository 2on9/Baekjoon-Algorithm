# 문제를 풀 때, T+20V 의 패널티가 추가된다고 한다. V는 바뀌지 않고, T만 추가되기 때문에 T에 대해 생각을 해보면 된다. 시간이 적게 걸리는 것부터 했을 경우, 10 20 30 -> 10 + (10 + 20) + (10 + 20 + 30) 이런식으로 패널티가 들어가지만 시간이 오래 걸리는 것부터 하게 되면 30 20 10 -> 30 + (30 + 20) + (30 + 20 + 10) 이런 식으로 들어가게 된다. 따라서 우리는 시간이 적게 걸리는 것부터 풀어나가야 된다.
D = [] 
cnt = 0
penalty = 0
for i in range(11):
    d, v = map(int, input().split())
    D.append(d)
    penalty += (20*v)
D.sort()
for j in D:
    penalty += (j + cnt)
    cnt = j + cnt
print(penalty)