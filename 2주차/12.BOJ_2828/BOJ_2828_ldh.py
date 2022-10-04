n, m = map(int, input().split())
j = int(input())

last = m
first = 1

apple = []

cnt = 0
i = 0

while True:
    apple.append(int(input()))
    i += 1
    if i > n:
        break

i = 0

while True:
    if last >= apple[i] >= first:
        continue
    elif end < apple[i]:
        cnt += apple[i] - last
        end = apple[i]
        start = end - m + 1
    elif start > apple[i]:
        cnt += first - apple[i]
        start = apple[i]
        end = start + m - 1
    if j < i:
        break

print(cnt)
