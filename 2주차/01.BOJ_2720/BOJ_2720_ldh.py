t = int(input())


for i in range(t):
    cnt_a, cnt_b, cnt_c, cnt_d = 0, 0, 0, 0
    n = int(input())
    if n >= 25:
        cnt_a = n // 25
        n = n % 25
    if n >= 10:
        cnt_b = n // 10
        n = n % 10
    if n >= 5:
        cnt_c = n // 5
        n = n % 5
    if n >= 1:
        cnt_d = n
        n == 0
    print(cnt_a, cnt_b, cnt_c, cnt_d)


