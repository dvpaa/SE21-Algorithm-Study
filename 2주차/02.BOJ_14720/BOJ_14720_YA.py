n = int(input())
milk = list(map(int, input().split()))
cnt = 0
for i in milk:
    if cnt % 3 == i:
        cnt += 1
print(cnt)
