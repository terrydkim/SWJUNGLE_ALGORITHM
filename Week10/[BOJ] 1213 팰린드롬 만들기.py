import sys
input = sys.stdin.readline

n = input().strip()
m = [0]* 26  # 알파벳 개수

for i in range(len(n)):
    m[ord(n[i])-65] += 1


cnt = 0
odd = ''
string = ''
for j in range(len(m)):
    if m[j] % 2 == 1:
        cnt += 1 
        odd = chr(65+j)
    string += m[j] // 2 * chr(65+j) # m[j] // 2 : 개수 반 짜르기 , chr(65+j): 알파벳 찾기

if cnt > 1:
    print("I'm Sorry Hansoo")

else:
    print(string + odd + string[::-1])

    
