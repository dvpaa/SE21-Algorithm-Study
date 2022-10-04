n,m = map(int,input().split())

a = [0 for i in range(m)]
b = [0 for i in range(m)]

for i in range(m):
    a[i],b[i] = map(int,input().split())

sm = min(b)
sm_s = min(a)

if sm * n > sm_s * (n//6 +1) and sm_s * (n//6) + sm * (n%6) > sm_s * (n//6 +1):
    print(sm_s * (n//6 +1))


elif sm * n > sm_s * (n//6) + sm * (n%6):
    print(sm_s * (n//6) + sm * (n%6))

else:
    print(sm * n)