t = int(input())
for i in range(t):
    c = int(input())
    qu = c//25
    c %= 25
    di = c//10
    c %= 10
    ni = c//5
    c %= 5
    pe = c
    print(qu,di,ni,pe)