# 판의 최대 크기 50*50 체스판 크기 8*8이므로 모든 위치를 다 탐색하고 최소 수정 횟수를 구하면 된다.
N, M = map(int, input().split())
board = []
result = []
for _ in range(N):
    board.append(input())
for a in range(N-7): # 체스판 크기는 8*8이므로 자를 수 있는 범위는 행, 열 -7까지
    for b in range(M-7):
        w_start = 0 # 시작이 w라고 가정한 완벽한 체스판 
        b_start = 0 # 시작이 b라고 가정한 완벽한 체스판
        for i in range(a, a+8): # 체스판 크기는 8*8이므로 탐색할 범위는 그 숫자에서 8칸씩
            for j in range(b, b+8):
                if (i+j) % 2 == 0: # (인덱스 00, 02, 04...)
                    if board[i][j] != 'W': # (w가 아니라면 시작이 w라고 가정한 완벽한 체스판에는 다시 칠해야 되는 것들이 생기게 되므로 w_index에 수정 횟수 추가)
                        w_start += 1
                    else: # (b가 아니라면 시작이 b라고 가정한 완벽한 체스판에는 다시 칠해야 되는 것들이 생기게 되므로 b_index에 수정 횟수 추가)
                        b_start += 1
                else: # (인덱스 01, 03, 05...)
                    if board[i][j] != 'W':  # (시작이 b라고 가정한 완벽한 체스판은 w가 와야 된다. w가 아니라면 다시 칠해야 되는 것들이 생기게 되므로 b_index에 수정 횟수 추가)
                        b_start += 1
                    else: # (시작이 w라고 가정한 완벽한 체스판은 b가 와야 된다. b가 아니라면 다시 칠해야 되는 것들이 생기게 되므로 w_index에 수정 횟수 추가)
                        w_start += 1
        result.append(min(w_start, b_start)) # 그 중 최소값을 추가해준다.
print(min(result)) # 모든 경우에서의 최소값중에서 가장 최소인 값이 정답이다.