n = int(input())
v = list(map(int, input().split()))
v.sort()
cost = 0

for i in range(len(v)-1):
    cost += v[i]

print(cost)