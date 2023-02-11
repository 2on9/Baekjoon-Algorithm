# 일수로 오름차순 정렬한 뒤, 맨 마지막 날(첫번째 인덱스)부터 점수가 높은 순서대로 과제를 하면 된다. -> 과제 마감일은 과제를 끝내는 날(=date)보다 크거나 작으면 할 수 있는 과제가 된다. 그 중에 높은 과제를 고르면 된다.
import sys
input = sys.stdin.readline

N = int(input())
assignment = [list(map(int, input().split())) for _ in range(N)]
assignment.sort(key=lambda x : -x[0]) # 일수로 오름차순 정렬

pose = [] # 가능한 과제 후보리스트
result = 0

for date in range(assignment[0][0], 0, -1): # 맨 마지막 날부터 1일차까지 거꾸로 채워나간다.
    while assignment and assignment[0][0] >= date: # 과제가 있고, 마감일이 실제 하는 날보다 크거나 같으면 할 수 있다.
        pose.append(assignment.pop(0)[1])
    if pose:
        pose.sort(reverse=True) # 후보리스트를 오름차순으로 정렬하여 점수가 가장 높은 과제를 선택한다.
        result += pose.pop(0) 
print(result)