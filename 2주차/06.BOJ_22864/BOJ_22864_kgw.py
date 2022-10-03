A, B, C, M = map(int, input().split())
tired = 0
cnt = 0
time = 0

while time < 24:
    if tired + A <= M:
        tired += A
        cnt += B
    else:
        tired = max(tired - C, 0)

    time += 1

print(cnt)
