# 가능한 앞쪽에 캠핑을 시도하면 된다.
num = 0 
while 1:
    L, P, V = map(int, input().split())
    if L+P+V == 0:
        break
    num += 1
    result = L * (V // P) + min(L, V % P)
    print('Case %d: %d' %(num, result))