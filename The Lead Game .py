#TLG
p1 = 0
p2 = 0
max1 = 0
max2 = 0
temp1 = 0
temp2 = 0
for _ in range(int(input())):
    a, b = map(int,input().split())
    a += temp1
    b += temp2
    if a > b:
        p1 += abs(a-b)
        if max1 < abs(a-b):
            max1 = abs(a-b)
    else:
        p2 += abs(a-b)
        if max2 < abs(a-b):
            max2 = abs(a-b)
    temp1 = a
    temp2 = b

if p1 > p2:
    print("1 %i" % max1)
else:
    print("2 %i" % max2)
        
