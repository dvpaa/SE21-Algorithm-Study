n = int(input())
mk = list(map(int,input().split()))
pre, ti = 2, 0

for i in mk:
    if pre == 2 and i == 0:
        pre = 0
        ti += 1
    elif pre == 0 and i == 1:
        pre = 1
        ti += 1
    elif pre == 1 and i ==2:
        pre = 2
        ti += 1
    else:
        continue
print(ti)
