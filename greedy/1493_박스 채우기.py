# 가장 큰 부피의 정육면체부터 작은 부피의 정육면체로 채워나가면 되는 문제이다(내림차순 정렬). 중요한 것은 이전 단계의 부피로 넘어갈 때마다 채운 부피의 8배를 해줘야 된다는 것이다. -> 기준점이 바뀐다, 2*2*2 = 8배 (정육면체 부피가 8배씩 감소하기 때문) 그렇게해서 결국 1x1x1 정육면체 기준까지 들어가면 총 개수를 구할 수 있다.
import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())
volume = length * width * height
n = int(input())
cube = sorted([tuple(map(int, input().split())) for _ in range(n)], reverse=True)
result = total_now = 0

for i, i_num in cube:
    total_now *= 8 # 이전 단계로 갈수록 지금까지 채운 부피는 8배가 된다. 만약 4x4x4 1개로 채웠다면 2x2x2기준으로 본다면 8개가 있다는 것이고, 1x1x1기준은 64개가 채워져 있다는 것이다. 
    i_len = 2**i

    cnt_limit = (length // i_len) * (width // i_len) * (height // i_len) - total_now
    cnt_limit = min(i_num, cnt_limit) 

    result += cnt_limit
    total_now += cnt_limit

if total_now == volume: # 부피와 total_now(1x1x1 정육면체 합)이 같으면 만들 수 있다.
    print(result)
else: # 다르다면 만들 수 없다.
    print(-1)