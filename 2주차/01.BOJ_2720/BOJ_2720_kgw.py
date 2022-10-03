coins = [25, 10, 5, 1]

for _ in range(int(input())):
    C = int(input())
    result = [0, 0, 0, 0]
    for idx, coin in enumerate(coins):
        result[idx] += C // coin
        C %= coin
    print(*result)
