# 센서들을 일직선 상에 오름차순 정렬했을 때, 집중국 개수로 구역을 잘라내면 그 구역에서의 센서들의 차이가 집중국과 센서거리의 최솟값이 나온다. 구역을 나눌때는 센서들의 거리 차이가 컸던 것부터 잘라준다.
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
censor = sorted(list(map(int, input().split())))
diff = []

if K >= N: # 센서 개수보다 집중국 개수가 많을 시에는 집중국을 센서에다가 설치하면 되므로 0이 된다.
    print(0)
else:  # 적을 시에는 구역을 K개로 나눠준다.
    for i in range(1, N):
        diff.append(censor[i] - censor[i-1])
    diff.sort(reverse=True)
    for _ in range(K-1): # 센서들간의 거리 차이 중 가장 큰 것부터 없앤다. (최솟값)
        diff.pop(0)

print(sum(diff))