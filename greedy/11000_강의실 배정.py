# 강의실의 개수를 최소로 하기 위해선, 먼저 빨리 시작하는 순서대로 정렬을 한 뒤 다음 수업이 끝나는 시간보다 빠른 경우 새로운 강의실을 추가해주고 느린 경우는 그 강의를 뺀 후, 새로운 강의를 넣어준다.
import sys
input = sys.stdin.readline
import heapq

N = int(input())
classroom = sorted(list(map(int, input().split())) for _ in range(N))
q = []
heapq.heappush(q, classroom[0][1])
for i in range(1, N):
    if classroom[i][0] < q[0]:
        heapq.heappush(q, classroom[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, classroom[i][1])
print(len(q))