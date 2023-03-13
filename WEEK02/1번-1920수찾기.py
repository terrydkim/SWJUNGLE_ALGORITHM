
N = input()
N_num = list(map(int,input().split()))

M = input()
M_num = list(map(int,input().split()))
N_num.sort()

def search(lst, key):

    pl = 0
    pr = len(lst)-1

    while True:
        pc = (pr+pl)//2
        if key == lst[pc]:
            return 1
        elif key > lst[pc]:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return 0

for i in M_num:
    print(search(N_num,i))

