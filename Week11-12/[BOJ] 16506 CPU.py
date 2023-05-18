import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    opcode, rD, rA, rB = input().strip().split()
    lst = ""
    if opcode == 'ADD' or opcode == 'ADDC':
        lst += '0000'
    elif opcode == 'SUB' or opcode == 'SUBC':
        lst += '0001'
    elif opcode == 'MOV' or opcode == 'MOVC':
        lst += '0010'
    elif opcode == 'AND' or opcode == 'ANDC':
        lst += '0011'
    elif opcode == 'OR' or opcode == 'ORC':
        lst += '0100'
    elif opcode == 'NOT':
        lst += '0101'
    elif opcode == 'MULT' or opcode == 'MULTC':
        lst += '0110'
    elif opcode == 'LSFTL' or opcode == 'LSFTLC':
        lst += '0111'
    elif opcode == 'LSFTR' or opcode == 'LSFTRC':
        lst += '1000'
    elif opcode == 'ASFTR' or opcode == 'ASFTRC':
        lst += '1001'
    elif opcode == 'RL' or opcode == 'RLC':
        lst += '1010'
    elif opcode == 'RR' or opcode == 'RRC':
        lst += '1011'
    if opcode[-1] =='C':
        bit = '1'
    else:
        bit = '0'
    lst += bit
    lst += '0'
    rD = format(int(rD),'03b')
    lst += str(rD)
    rA = format(int(rA),'03b')
    lst += str(rA)
    if bit == '0':
        rB = format(int(rB),'03b')
        lst += str(rB)
        lst += '0'
    else:
        rB = format(int(rB),'04b')
        lst += str(rB)
        
    print(lst)