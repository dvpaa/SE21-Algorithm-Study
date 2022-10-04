case = 0
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    case += 1
    print(f"Case {case}:", V // P * L + L if V % P >= L else V // P * L + V % P)
