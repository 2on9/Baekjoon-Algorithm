# 일수로 오름차순 정렬한 뒤 뒤에 날짜부터 (date = N)
import sys
input = sys.stdin.readline

N = int(input())
assignment = [list(map(int, input().split())) for _ in range(N)]
assignment.sort(key=lambda x : -x[0])

pose = [] # 가능한 과제
result = 0

for date in range(assignment[0][0], 0, -1):
    while assignment and assignment[0][0] >= date:
        pose.append(assignment.pop(0)[1])
    if pose:
        pose.sort(reverse=True)
        result += pose.pop(0)
print(result)