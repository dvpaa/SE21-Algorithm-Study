n = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
del a[0]

print(sum(a))
