n = int(input())
t = sorted(list(map(int, input().split())), reverse=True)

for i in range(n):
    t[i] += i + 1

print(max(t) + 1)
