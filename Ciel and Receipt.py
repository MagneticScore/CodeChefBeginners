#CIELRCPT

for _ in range(int(input())):
    p = int(input())
    c = 0
    while p > 2048:
        c += 1
        p -= 2048
    else:
        p = bin(p)
        l = p[2:]
        for x in l:
            c += int(x)
        print(c)
