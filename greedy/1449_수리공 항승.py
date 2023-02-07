# 좌우 0.5만큼 간격을 줘야 되므로 시작은 첫 인덱스에서 -0.5를 해준다. 그 다음은 L만큼 더 했을 때(테이프 붙힘), 이것이 그 다음 인덱스 +0.5보다 크거나 같으면 다음으로 넘어가고 작으면 새로운 테이프를 추가해주고 시작지점을 바꿔준다. 
N, L = map(int, input().split())
leak = list(map(int,(input().split())))
leak.sort() # 순서가 뒤죽박죽 나오므로 오름차순으로 정렬해준다.

cnt = 1
start = leak[0] - 0.5 

for i in range(1, N):
    if start + L >= leak[i] + 0.5: # 시작지점에서 붙힌 테이프가 다음 인덱스보다 크거나 같다면 (테이프가 남거나 딱 맞는다면)
        continue
    else: # 시작지점에서 붙힌 테이프가 다음 인덱스보다 작다면 (테이프가 부족하다면)
        start = leak[i] - 0.5 
        cnt += 1
print(cnt)