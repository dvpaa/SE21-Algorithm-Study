n = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)

for i in range(n):
    a[i] = a[i]+2+i

print(max(a))