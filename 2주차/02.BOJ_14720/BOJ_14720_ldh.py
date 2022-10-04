# 가게 수
n = int(input())
# 가게 종류
m = list(map(int, input().split()))

cnt = 0

for i in range(n):
    # 0%3=0 / 1%3=1 / 2%3=2
    if m[i] == cnt % 3:
        cnt += 1

print(cnt)
