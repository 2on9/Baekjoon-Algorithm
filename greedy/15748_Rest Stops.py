import sys
input = sys.stdin.readline

L, N, j, b = map(int, input().split())
rest = [list(map(int, input().split())) for _ in range(N)]
rest.sort(key=lambda x: -x[1])
taste = stop = 0
diff = j-b

for i in range(N):
    if rest[i][0] >= stop:
        taste += rest[i][1] * (diff*(rest[i][0]-stop))
        stop = rest[i][0]
    else:
        pass
print(taste)

