n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
cnt = 0
for i in reversed(a):
    cnt += k // i
    k %= i
print(cnt)
