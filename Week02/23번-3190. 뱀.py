from collections import deque

# 게임 보드 초기화
n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 1

# 사과 위치 초기화
k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 2

# 뱀 초기화
snake = deque([(0, 0)])

# 이동 방향 초기화 (오른쪽부터 반시계방향)
dy = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dx = [0, 1, 0, -1]
direction = 1

# 뱀의 방향 변환 정보 입력
l = int(input())
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 게임 시작
time = 0
info_idx = 0
while True:
    # 다음 이동할 위치
    ny = snake[-1][0] + dy[direction]
    nx = snake[-1][1] + dx[direction]
    time += 1

    # 게임 종료 조건
    if ny < 0 or ny >= n or nx < 0 or nx >= n or board[ny][nx] == 1:
        break

    # 이동할 위치에 사과가 있는 경우
    if board[ny][nx] == 2:
        board[ny][nx] = 1
        snake.append((ny, nx))
    # 이동할 위치에 사과가 없는 경우
    else:
        board[ny][nx] = 1
        snake.append((ny, nx))
        y, x = snake.popleft()
        board[y][x] = 0

    # 방향 전환 조건
    if info_idx < l and time == info[info_idx][0]:
        if info[info_idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        info_idx += 1

# 게임 종료 출력
print(time)
