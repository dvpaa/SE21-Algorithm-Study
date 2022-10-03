i = 1

while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    if V % P < L:
        print(f"Case {i}: {V // P * L + V % P}")
    else:
        print(f"Case {i}: {V // P * L + L}")
    i += 1