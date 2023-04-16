import sys
input = sys.stdin.readline

n = int(input())

line = 0  # 대각 라인
index = 0 # 라인 마지막 인덱스

while n > index:
    line += 1
    index += line

diff = index - n
# 대각 라인 짝수면 위에서 내려옴
if line % 2 == 0: 
    top = line - diff
    bottom = diff + 1
# 홀수면 올라감
elif line % 2 != 0:
    top = diff + 1
    bottom = line - diff

print(f'{top}/{bottom}')