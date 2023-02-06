# 시간복잡도는 O(n^3)이지만 n이 45로 45^3 = 91125 이 나오기 때문에 1초 이내로 끝낼 수 있다. 

triangle = [n*(n+1)//2 for n in range(1, 46)] # 45*46/2 = 1025 > 1000
eureka = [0 for _ in range(1001)]

# 미리 1000 이하의 유레카 수를 구한다.
for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000: # index range가 초과하면 안 되므로 if 설정
                eureka[i+j+k] = 1 

T = int(input())
for _ in range(T):
    print(eureka[int(input())])