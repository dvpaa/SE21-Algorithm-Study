N = int(input())
Da = int(input())
p = []
cnt = 0

for i in range(N-2):
    p.append(int(input()))

while True:
    p.sort()
    if Da <= max(p):
        Da += 1
        p[(N-2)-1] += p[(N-2)-1]
        cnt += 1

    elif Da > max(p):
        break

