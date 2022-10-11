N = int(input())
C = sorted(list(list(map(int, input().split())) for _ in range(N)), key=lambda x: x[0])
C = sorted(C, key=lambda x: x[1])
for i in C:
    print(*i)
