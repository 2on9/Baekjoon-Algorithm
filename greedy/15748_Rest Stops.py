# B가 J보다 빠르게 가서 taste 점수가 높은 휴게소에 오래 있으면 된다. taste 점수가 가장 높은 휴게소를 먼저 들른 뒤, J가 오면 그 다음으로 높은 휴게소를 가면 된다. -> 지나친 곳이라면 그냥 패스하고 지나치지 않았으면 들려서 taste 점수를 획득한다.
import sys
input = sys.stdin.readline

L, N, j, b = map(int, input().split())
rest = [list(map(int, input().split())) for _ in range(N)]
rest.sort(key=lambda x: -x[1]) # taste 점수를 오름차순으로 정렬
taste = stop = 0
diff = j-b

for i in range(N):
    if rest[i][0] >= stop: # 지금 멈춘 곳(현재 위치)보다 크거나 같으면 들려서 taste 점수를 얻는다.
        taste += rest[i][1] * (diff*(rest[i][0]-stop)) 
        stop = rest[i][0]
    else:
        pass
print(taste)